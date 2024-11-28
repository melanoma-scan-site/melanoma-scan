<script>
	import ResultsCard from '$lib/components/app/resultsCard.svelte';
	import UploadCard from '$lib/components/app/uploadCard.svelte';
	import StepProgress from '$lib/components/app/stepProgress.svelte';
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';

	let disclaimerAccepted = $state(false);
	let currentStep = $state(1);
	let selectedFile = $state(null);

	// Results from AI prediction
	let detectionConfidence = $state(0);
	let melanomaDetected = $state(false);
</script>

<main class="flex flex-grow flex-col items-center justify-center gap-y-6 py-6 md:px-6">
	<!-- Disclaimer alert that the user has to accept before using the site -->
	{#if !disclaimerAccepted}
		<AlertDialog.Root open={!disclaimerAccepted}>
			<AlertDialog.Content>
				<AlertDialog.Header>
					<AlertDialog.Title>Important Medical Disclaimer</AlertDialog.Title>
					<AlertDialog.Description>
						This AI-powered tool is designed to assist in preliminary melanoma screening only and
						should not replace professional medical diagnosis. The analysis provided is not a
						substitute for consultation with a qualified healthcare provider. Please seek immediate
						medical attention if you have concerns about your skin condition.
					</AlertDialog.Description>
				</AlertDialog.Header>
				<AlertDialog.Footer>
					<AlertDialog.Action
						onclick={() => {
							disclaimerAccepted = true;
						}}>I Understand</AlertDialog.Action
					>
				</AlertDialog.Footer>
			</AlertDialog.Content>
		</AlertDialog.Root>
	{/if}

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
