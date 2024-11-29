<script>
	import * as Card from '$lib/components/ui/card/index.js';
	import * as Accordion from '$lib/components/ui/accordion/index.js';

	import { ArrowLeft } from 'lucide-svelte';
	import { Button } from '$lib/components/ui/button/index.js';
</script>

<main class="flex flex-grow flex-col items-center justify-center gap-y-6 py-6 md:px-6">
	<div class="w-11/12 space-y-3 md:w-4/12">
		<Button href="/" class="p4" variant="outline" size="icon"><ArrowLeft /></Button>
		<Card.Root>
			<Card.Header>
				<Card.Title>FAQ</Card.Title>
				<Card.Description>
					Common questions about our melanoma detection tool, data privacy and AI accuracy etc. If
					you can't find what you're looking for, feel free to contact us.
				</Card.Description>
			</Card.Header>
			<Card.Content>
				<Accordion.Root type="single">
					<Accordion.Item value="upload-methods">
						<Accordion.Trigger>How can I upload my images?</Accordion.Trigger>
						<Accordion.Content>
							There are three easy ways to upload your images: 1. Drag and drop your image directly
							onto the upload area 2. Click "Choose file" to select an image from your device 3. On
							mobile devices, you can use your camera to take a photo directly using the "capture"
							feature
						</Accordion.Content>
					</Accordion.Item>

					<Accordion.Item value="privacy">
						<Accordion.Trigger>How is my data handled and protected?</Accordion.Trigger>
						<Accordion.Content>
							We do not store any images or personal data on our servers. All image processing is
							done in real-time, and the data is immediately discarded after analysis. Your privacy
							and security are our top priorities.
						</Accordion.Content>
					</Accordion.Item>

					<Accordion.Item value="accuracy">
						<Accordion.Trigger>How accurate is the AI detection?</Accordion.Trigger>
						<Accordion.Content>
							While our AI model is trained on a large dataset of melanoma images, it should not be
							considered a replacement for professional medical diagnosis. The confidence percentage
							provided is an estimate, and we strongly recommend consulting a healthcare
							professional for proper evaluation.
						</Accordion.Content>
					</Accordion.Item>

					<Accordion.Item value="images">
						<Accordion.Trigger>What type of images should I upload?</Accordion.Trigger>
						<Accordion.Content>
							For best results, upload clear, well-lit photos of the skin area you want to analyze.
							The image should be in JPEG or PNG format and under 60MB in size. Ensure the
							suspicious area is centered and in focus.
						</Accordion.Content>
					</Accordion.Item>

					<Accordion.Item value="report">
						<Accordion.Trigger>Can I save or share my results?</Accordion.Trigger>
						<Accordion.Content>
							Yes, you can download your results as a PDF report that includes the analysis details
							and the uploaded image. This report can be shared with your healthcare provider, but
							remember it should only be used as a preliminary screening tool.
						</Accordion.Content>
					</Accordion.Item>

					<Accordion.Item value="cost">
						<Accordion.Trigger>Is this service free to use?</Accordion.Trigger>
						<Accordion.Content>
							Yes, this service is completely free to use. We believe in making preliminary melanoma
							screening tools accessible to everyone. However, we emphasize that this tool should
							not replace regular skin checks by qualified medical professionals.
						</Accordion.Content>
					</Accordion.Item>
				</Accordion.Root>
			</Card.Content>
		</Card.Root>
	</div>
</main>
