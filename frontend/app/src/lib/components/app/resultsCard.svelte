<script>
	import ArcChart from '$lib/components/app/arcChart.svelte';
	import * as Card from '$lib/components/ui/card/index.js';
	import { File, CircleHelp, Download, ArrowLeft } from 'lucide-svelte';
	import { jsPDF } from 'jspdf';
	import { Button } from '$lib/components/ui/button/index.js';

	let {
		detectionConfidence = 0,
		melanomaDetected = false,
		selectedFile = $bindable(),
		currentStep = $bindable()
	} = $props();

	// Generate a PDF report containing melanoma scan results, medical disclaimer, and analyzed preview image if available
	async function generatePDF() {
		const doc = new jsPDF();

		doc.setFontSize(16);
		doc.text('Melanoma Detection Results', 105, 20, { align: 'center' });

		doc.setFontSize(12);
		doc.text('Disclaimer: This is an AI-assisted analysis and should not be', 20, 40);
		doc.text(
			'considered as a medical diagnosis. Please consult a healthcare professional.',
			20,
			50
		);

		doc.text(`Detection Confidence: ${detectionConfidence}%`, 20, 70);
		doc.text(`Melanoma Detected: ${melanomaDetected ? 'Yes' : 'No'}`, 20, 80);

		if (selectedFile) {
			const reader = new FileReader();
			reader.onload = function () {
				doc.addImage(reader.result, 'JPEG', 20, 100, 170, 150);
				doc.save('melanoma-scan-results.pdf');
			};
			reader.readAsDataURL(selectedFile);
		} else {
			doc.save('melanoma-scan-results.pdf');
		}
	}

	// Reset so it shows upload card and removes the uploaded file
	function reset() {
		currentStep = 1;
		selectedFile = null;
	}
</script>

<!-- Card component -->
<Card.Root class="w-11/12 md:w-4/12">
	<Card.Content>
		<Button class="p4" variant="outline" size="icon" onclick={reset}><ArrowLeft /></Button>

		<!-- Arc chart component -->
		<div class="h-60 p-4">
			<ArcChart {detectionConfidence} {melanomaDetected} />
		</div>

		<!-- Medical disclaimer -->
		<div class="mt-7 w-full gap-y-2 text-pretty rounded-2xl bg-muted p-4">
			<p class="text-sm text-muted-foreground">
				Based on the image provided, the AI analysis suggests a <span class="font-bold"
					>{detectionConfidence}%</span
				> likelihood of melanoma. However, please remember this is only an AI-based estimate and not
				a medical diagnosis. For accurate results and peace of mind, consult a healthcare professional
				for a thorough evaluation. Early detection and expert advice are key to effective care.
			</p>
		</div>

		<!-- Preview of PDF containing results, can be downloaded with generatePDF call -->
		<div class="mt-7 flex w-full flex-col gap-y-2 rounded-2xl bg-muted p-4">
			<div class="flex items-center gap-x-2">
				<File size={40} strokeWidth={1} />
				<div class="flex w-full items-center justify-between">
					<div class="grid">
						<p class="font-bold">melanoma-scan-results.pdf</p>
						<p class="text-sm text-muted-foreground">
							{selectedFile &&
								(selectedFile.size > 1024 * 1024
									? Math.round((selectedFile.size + 3686) / (1024 * 1024)) + ' MB'
									: Math.round((selectedFile.size + 3686) / 1024) + ' KB')}
						</p>
					</div>

					<button class="transition-colors hover:text-muted-foreground" onclick={generatePDF}
						><Download size={25} /></button
					>
				</div>
			</div>
		</div>
	</Card.Content>
	<Card.Footer>
		<!-- Redirect to help page -->
		<div class="mt-3 flex w-full justify-start">
			<a
				class="inline-flex gap-x-2 text-muted-foreground transition-colors hover:text-indigo-500"
				href="/help"><CircleHelp />Help</a
			>
		</div>
	</Card.Footer>
</Card.Root>
