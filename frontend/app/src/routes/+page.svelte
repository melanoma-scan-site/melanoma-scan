<script>
	import { Sun, Moon, FileUp, File, X, CircleHelp, Check } from 'lucide-svelte';
	import { toggleMode } from 'mode-watcher';
	import { toast } from 'svelte-sonner';

	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Progress } from '$lib/components/ui/progress/index.js';
	import { Separator } from '$lib/components/ui/separator/index.js';

	const MAX_SIZE_MB = 60;
	const MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024;
	const ALLOWED_TYPES = ['image/jpeg', 'image/png'];

    let isDisclaimerAccepted = $state(false);
	let dragOver = $state(false);
	let currentStep = $state(1);
	let loading = $state(false);
	let uploadProgress = $state(0);
	let selectedFile = $state(null);
    let isResults = $state(false);
    let prediction = $state(0);
    let isMelanoma = $state(false);

	function createFileReader(file) {
		return new Promise((resolve, reject) => {
			const reader = new FileReader();
			reader.onload = () => resolve(reader.result);
			reader.onerror = () => reject(new Error('File reading failed'));
			reader.readAsDataURL(file);
		});
	}

	async function uploadImage(base64) {
		const xhr = new XMLHttpRequest();

		return new Promise((resolve, reject) => {
			xhr.upload.onprogress = (event) => {
				if (event.lengthComputable) {
					uploadProgress = Math.round((event.loaded / event.total) * 100);
				}
			};

			xhr.onload = () => {
				if (xhr.status === 200) {
					resolve(JSON.parse(xhr.response));
				} else {
					reject(new Error('Upload failed'));
				}
			};

			xhr.onerror = () => reject(new Error('Upload failed'));

			xhr.open('POST', 'https://melanoma-scan.site/check');
			xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
			xhr.send(`base64_file=${encodeURIComponent(base64)}`);
		});
	}

	async function handleFile(file) {
		if (!file) return;

		if (!ALLOWED_TYPES.includes(file.type)) {
			toast.error('Only JPEG and PNG files are allowed');
			return;
		}

		if (file.size > MAX_SIZE_BYTES) {
			toast.error(`File must be under ${MAX_SIZE_MB}MB`);
			return;
		}

		try {
			loading = true;
			uploadProgress = 0;
			selectedFile = file;

			const base64 = await createFileReader(file);

            // prepare to correct base64 format
            const base64Parts = base64.split(',', 2);
			let results = await uploadImage(base64Parts[1]);

            // set results to true
            isResults = true;
            isMelanoma = results['is_melanoma'];
            prediction = results['percent'];

			currentStep = 2;
		} catch (error) {
			console.error('Upload failed:', error);
			toast.error('Failed to process image');
			currentStep = 1;
			selectedFile = null;
		} finally {
			loading = false;
			uploadProgress = 0;
		}
	}
</script>

<main class="flex min-h-screen flex-col items-center justify-center gap-y-6">
	<!-- Disclaimer -->
    {#if isDisclaimerAccepted === false}
	<div class="bg-muted w-11/12 rounded-2xl p-4 text-sm md:w-4/12 flex flex-col">
		<h2 class="font-bold text-center">Disclaimer</h2>
		<p
			class="text-muted-foreground mt-4"
		>
			This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always
			seek the advice of your physician or other qualified health provider with any questions you
			may have regarding a medical condition. Never disregard professional medical advice or delay
			in seeking it because of something you have read on this website.
		</p>

        <!-- button to accept -->
        <button
            class="btn btn-blue mt-4 block text-right"
            onclick={() => {
                isDisclaimerAccepted = true;
                console.log(isDisclaimerAccepted);
            }}>
            <span>
                <Check class='inline' />
            </span>
        </button>
	</div>
    {/if}

    {#if isDisclaimerAccepted === true}
	<!-- Step indication/progress component -->
	<div class="pointer-events-none flex w-11/12 items-center justify-center gap-2 md:w-4/12">
		{#each ['Upload file', 'Results'] as step, i}
			{#if i > 0}
				<Separator class="w-8" />
			{/if}
			<div class="inline-flex items-center gap-x-2">
				<Button disabled={currentStep < i + 1} class="size-8">
					{#if currentStep > i + 1 || (currentStep === 2 && i === 1)}
						<Check />
					{:else}
						{i + 1}
					{/if}
				</Button>
				<p class={currentStep === i + 1 ? 'font-bold' : ''}>{step}</p>
			</div>
		{/each}
	</div>

	<!-- Step 1 card: Upload image -->
	<Card.Root class="w-11/12 md:w-4/12">
		<Card.Content>
			<label
				class="group relative flex h-56 w-full flex-col items-center justify-center gap-y-2 rounded-2xl border-[2.3px] border-dashed transition-colors {dragOver
					? 'border-blue-500 bg-blue-500/5'
					: 'border-black hover:border-blue-500 hover:bg-blue-500/5'}"
				ondragenter={(e) => {
					e.preventDefault();
					dragOver = true;
				}}
				ondragleave={(e) => {
					e.preventDefault();
					dragOver = false;
				}}
				ondragover={(e) => e.preventDefault()}
				ondrop={(e) => {
					e.preventDefault();
					dragOver = false;
					handleFile(e.dataTransfer?.files[0]);
				}}
			>
				<input
					type="file"
					accept={ALLOWED_TYPES.join(',')}
					capture="environment"
					class="hidden"
					onchange={(e) => handleFile(e.currentTarget.files?.[0])}
					disabled={loading}
				/>

				<div class="pointer-events-none flex flex-col items-center gap-y-4">
					<FileUp
						class="transition-colors {dragOver ? 'text-blue-500' : 'group-hover:text-blue-500'}"
						size={70}
						strokeWidth={0.5}
					/>
					<p>
						{loading ? 'Processing...' : 'Drag and Drop file here or'}
						<span class="font-bold">Choose file</span>
					</p>
				</div>
			</label>

			<div class="text-muted-foreground mt-3 flex justify-between text-sm">
				<p>Supported formats: JPEG, PNG</p>
				<p>Maximum size: {MAX_SIZE_MB} MB</p>
			</div>

			{#if selectedFile}
				<div class="bg-muted mt-10 flex w-full flex-col gap-y-2 rounded-2xl p-4">
					<div class="flex items-center gap-x-2">
						<File size={45} strokeWidth={1} />
						<div class="grid">
							<p class="font-bold">{selectedFile.name}</p>
							<p class="text-muted-foreground text-sm">
								{Math.round(selectedFile.size / (1024))} KB
							</p>
						</div>
					</div>
					{#if loading}
						<Progress class="bg-zinc-200" value={uploadProgress} />
					{/if}
				</div>
			{/if}

            {#if isResults === true}
                <!-- show is melanoma results -->
                <div>
                    {#if isMelanoma === false}
                        <h2 class="font-bold text-center mt-4 text-green-700">Prediction for melanoma {prediction}%</h2>
                        <div class="bg-muted w-full rounded-2xl p-4 text-sm flex flex-col">
                            <p class="text text-green-700">
                                The image you uploaded is not a melanoma.                                
                            </p>
                            <br/>
                            
                            <p>
                                <!-- disclaimer -->
                                <span class="text-muted-foreground">
                                    This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always
                                    seek the advice of your physician or other qualified health provider with any questions you
                                    may have regarding a medical condition. Never disregard professional medical advice or delay
                                    in seeking it because of something you have read on this website.
                                </span>
                            </p>
                        </div>
                    {/if}
                    {#if isMelanoma === true}
                        <h2 class="font-bold text-center mt-4 text-red-700">Prediction for melanoma {prediction}%</h2>
                        <div class="bg-muted w-full rounded-2xl p-4 text-sm flex flex-col">
                            <p class="text text-red-700">
                                The image you uploaded is a melanoma.                                
                            </p>
                            <br/>
                            <p>
                                <span class="text-red-700">
                                    Please consult a doctor immediately.
                                </span>
                            </p>
                            <br/>
                            
                            <p>
                                <!-- disclaimer -->
                                <span class="text-muted-foreground">
                                    This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always
                                    seek the advice of your physician or other qualified health provider with any questions you
                                    may have regarding a medical condition. Never disregard professional medical advice or delay
                                    in seeking it because of something you have read on this website.
                                </span>
                            </p>
                        </div>
                    {/if}
                </div>
            {/if}
		</Card.Content>
	</Card.Root>
    {/if}

</main>
