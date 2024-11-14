<script>
	import { Sun, Moon, FileUp, File, X, CircleHelp, Check } from 'lucide-svelte';
	import { toggleMode } from 'mode-watcher';
	import { Button } from '$lib/components/ui/button/index.js';

	import * as Card from '$lib/components/ui/card/index.js';
	import { Progress } from '$lib/components/ui/progress/index.js';
	import { Separator } from '$lib/components/ui/separator/index.js';

	let currentStep = $state(1);
	let validFileAdded = $state(false);
</script>

<main class="flex min-h-screen flex-col items-center justify-center gap-y-6">
	<!-- Step indication/progress component -->
	<div class="pointer-events-none flex w-11/12 items-center justify-center gap-2 md:w-4/12">
		{#each ['Upload file', 'Analyze image', 'Results'] as step, i}
			{#if i > 0}
				<Separator class="w-8" />
			{/if}
			<div class="inline-flex items-center gap-x-2">
				<Button disabled={currentStep < i + 1} class="size-8">
					{#if currentStep > i + 1 || (currentStep === 3 && i === 2)}
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
			<!-- Image upload field -->
			<div
				class="group flex h-56 w-full flex-col items-center justify-center gap-y-2 rounded-2xl border-[2.3px] border-dashed border-black transition-colors hover:border-blue-500 hover:bg-blue-500/5"
			>
				<FileUp class="transition-colors group-hover:text-blue-500" size={70} strokeWidth={0.5} />
				<p>Drag and Drop file here or <span class="font-bold">Choose file</span></p>
			</div>

			<!-- Image formats and max size allowed text -->
			<div class="mt-3 flex justify-between text-sm text-muted-foreground">
				<p>Supported formats: JPEG, PNG</p>
				<p>Maximum size: 60 MB</p>
			</div>

			<!-- Uploaded file details preview -->
			<div class="mt-10 flex w-full flex-col gap-y-2 rounded-2xl bg-muted p-4">
				<div class="flex items-center gap-x-2">
					<File size={45} strokeWidth={1} />
					<div class="grid">
						<p class="font-bold">IMG_3242.png</p>
						<p class="text-sm text-muted-foreground">19 MB</p>
					</div>
				</div>
				<!-- Note: change bg color for dark mode as well -->
				<Progress class="bg-zinc-200" value={61} />
			</div>
		</Card.Content>
		<Card.Footer>
			<div class="mt-3 flex w-full justify-between">
				<a class="inline-flex gap-x-2 text-muted-foreground" href="/help"><CircleHelp />Help</a>
				<Button disabled={!validFileAdded}>Next</Button>
			</div>
		</Card.Footer>
	</Card.Root>
</main>
