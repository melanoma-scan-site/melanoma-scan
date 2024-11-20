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

	let dragOver = $state(false);
	let currentStep = $state(1);
	let loading = $state(false);
	let uploadProgress = $state(0);
	let selectedFile = $state(null);

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

			xhr.open('POST', 'https://melanoma-scan.site/api/test');
			xhr.setRequestHeader('Content-Type', 'application/json');
			xhr.send(JSON.stringify({ image: base64 }));
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
			await uploadImage(base64);

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
								{Math.round(selectedFile.size / (1024 * 1024))} MB
							</p>
						</div>
					</div>
					{#if loading}
						<Progress class="bg-zinc-200" value={uploadProgress} />
					{/if}
				</div>
			{/if}
		</Card.Content>
		<Card.Footer>
			<div class="mt-3 flex w-full justify-start">
				<a class="text-muted-foreground inline-flex gap-x-2" href="/help"><CircleHelp />Help</a>
			</div>
		</Card.Footer>
	</Card.Root>
</main>
