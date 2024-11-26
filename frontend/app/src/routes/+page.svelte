<script>
	import ResultsCard from '$lib/components/app/resultsCard.svelte';
	import UploadCard from '$lib/components/app/uploadCard.svelte';
	import StepProgress from '$lib/components/app/stepProgress.svelte';

	let currentStep = $state(1);
	let selectedFile = $state(null);

	// Results from AI prediction
	let detectionConfidence = $state(0);
	let melanomaDetected = $state(false);
</script>

<main class="flex flex-grow flex-col items-center justify-center gap-y-6 py-6 md:px-6">
	<!-- Step indication/progress component -->
	<StepProgress {currentStep} />

	{#if currentStep === 1}
		<!-- Step 1 card: Upload image -->
		<UploadCard bind:currentStep bind:selectedFile bind:detectionConfidence bind:melanomaDetected />
	{:else if currentStep === 2}
		<!-- Step 2 card: AI results -->
		<ResultsCard {detectionConfidence} {melanomaDetected} bind:selectedFile bind:currentStep />
	{/if}
</main>
