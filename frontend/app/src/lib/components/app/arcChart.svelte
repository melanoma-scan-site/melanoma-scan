<script>
	import { Arc, Chart, Svg, Text } from 'layerchart';
	import { cls } from '@layerstack/tailwind';
	import { cubicInOut } from 'svelte/easing';

	let { detectionConfidence = 0 } = $props();
</script>

<!-- Arc chart that shows the AI detection confidence in percentage  -->
<Chart>
	<Svg center>
		<Arc
			initialValue={0}
			value={detectionConfidence}
			innerRadius={-20}
			cornerRadius={4}
			class="fill-indigo-500"
			track={{ class: 'fill-zinc-500/10' }}
			tweened={{ duration: 700, easing: cubicInOut }}
		>
			<Text
				value={Math.round(detectionConfidence ?? 0)}
				textAnchor="middle"
				verticalAnchor="middle"
				dy={16}
				class="text-6xl tabular-nums dark:text-white"
				fill="currentColor"
			/>
		</Arc>
	</Svg>
</Chart>
