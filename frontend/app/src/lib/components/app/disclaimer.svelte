<script>
	let { currentStep = $bindable() } = $props();
</script>

<div class="bg-muted flex w-11/12 flex-col rounded-2xl p-4 text-sm md:w-4/12">
	<h2 class="text-center font-bold">Disclaimer</h2>
	<p class="text-muted-foreground mt-4">
		This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always
		seek the advice of your physician or other qualified health provider with any questions you may
		have regarding a medical condition. Never disregard professional medical advice or delay in
		seeking it because of something you have read on this website.
	</p>

	<!-- button to accept -->
	<button
		class="btn btn-blue mt-4 block text-right"
		onclick={() => {
			currentStep = 1;
		}}
	>
		<span> Accept </span>
	</button>
</div>
