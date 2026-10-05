---
title: "Programmatic Product Launch Film"
category: "video-production"
tags: ["launch-film", "motion-design", "programmatic-video", "voiceover", "audio-sync", "playwright", "ffmpeg", "brand-film"]
description: "Creates a fully coded product launch film with voiceover, music synchronization, scene choreography, sound design, deterministic rendering, and visual QA."
version: "1.0"
---

# Programmatic Product Launch Film

## 🎯 Overview
Creates a fully coded product launch film with voiceover, music synchronization, scene choreography, sound design, deterministic rendering, and visual QA. Preserves the complete production architecture while generalizing product-specific inputs.

## 📋 Prompt
```text
<inputs>
Ask me for: my product's name, a one-line pitch, my logo, 3-6 screenshots of my product, 40+ images of what it makes (or photos of it), my brand colours and font, an ElevenLabs API key and voice ID, and a royalty-free song with a clear drop (the file and the drop's timestamp).

If I skip any, use these defaults:

- Product name: [DEFAULT PRODUCT NAME]
- Pitch: [DEFAULT ONE-LINE PITCH]
- Images: free Unsplash and Pixabay images appropriate to the product
- Font: [DEFAULT FONT, e.g. Geist]
- Ink: [DEFAULT INK COLOUR, e.g. #111214]
- Voice: [DEFAULT ELEVENLABS VOICE + VOICE ID]
- ElevenLabs model: [DEFAULT VOICE MODEL]
- Music: [DEFAULT ROYALTY-FREE TRACK]
- BPM: [TRACK BPM]
- Drop: [DROP TIMESTAMP]
</inputs>

<script>
Write a 9-line voiceover in this shape and map every line to my product:

"This is [name]. A [category]... made for [value]. [Verb] in ANY style. Show it a [input] — and it just... gets you. The more you use it, the BETTER it gets. Tune its [setting]. Its [setting]. Its [setting]. Every [output] — exactly how you see it. [Name]. Out now."

Light emotion tags only: [softly] on the quiet lines, [excited] on the [Verb] line.

The opener gets no tag and a plain full stop.
</script>

<voice>
Call the ElevenLabs API directly with my key, no MCP.

Generate 4 takes of the whole script in one read and let me pick.

If one line is off, regenerate only that line 4 times and splice the best one into my take.

Cut every pause over 0.28s down to 0.2s, then level each phrase 85% of the way to the median level, changing gain only inside the pauses.

For word timings, cut the read at every pause of 100ms or more, transcribe each chunk on its own with Whisper and pin each chunk's first word to its measured onset.

One Whisper pass puts words up to half a second late.
</voice>

<direction>
A [DURATION, default 22 seconds] [ASPECT RATIO, default square] launch film, [RESOLUTION, default 1440x1440] at [FPS, default 60fps], in the style of [VISUAL DIRECTION / BRAND FILM STYLE].

Default visual direction:

A white page, one typeface, black ink, real images, and every caption typed word by word at the exact moment it's spoken.

Every control ([PRODUCT-SPECIFIC CONTROLS]) is liquid glass: the scene behind it frosted, its edge bending that scene like thick glass, a top sheen, a bright rim and a soft lift shadow.

Glass on plain white shows nothing, so put a slow pastel aura in my brand colours, or a blurred wash of the photo, behind it.

The one word she stresses types in a gradient of my brand colours with a faint glow behind it.

Motion rules:

- the camera always drifts (a 1.0 to 1.04 push per scene)
- when one scene hands its content to the next, the next starts at the zoom the last one ended on
- nothing pops in
- fades are at least 0.3s and eased
- images switch on 16th notes with a click each
- scene changes land on phrase starts
- the music's drop lands on the [Verb] line
- no full stops on screen

Banned:

- selection-box highlights
- beat-snapped slams
- white flashes
- 3D
- templates
</direction>

<structure>
Seven scenes, each hung on the voice:

1. "This is [name]": a collage of my images drifts out as the name types in big, then the category line replaces it.

2. "made for [value]": full-bleed flashes of my best images on 16th notes into the drop, with the line typed over them in white.

3. The drop: [PRODUCT'S PRIMARY INPUT CONTROL] demonstrates a short real interaction, then the result switches or evolves on every 16th, with supporting labels or thumbnails where appropriate.

4. "Show it a [input]": [NUMBER] input/reference images move into a clear composition around the result as the product-understanding line types.

5. "The more you use it, the better it gets": two typed lines, the stressed word in the brand gradient.

6. The settings: show 3 real product settings or controls, each moving as she names it. The output visibly responds to each setting.

7. "Every [output], exactly how you see it": a large collection of my real outputs bursts from the centre behind a glass caption pill, then collapses into my logo as the name types, with "Out now" underneath. Hold 2s.

Swap the prompt bar, results, sliders, and any other generic controls for my product's real input, outputs, settings, and interaction model.
</structure>

<sound>
Start the song so its drop lands on the [Verb] line, and anchor the beat grid there.

Duck the music under the voice with a 3-band sidechain:

- lows 30%
- mids 85%
- air 55%
- 0.3s hold
- 50ms look-ahead
- 0.5s release

Then move each phrase's mids until the voice sits about 9 dB over the music between 300 Hz and 4 kHz.

One downloaded [SFX SOURCE, default Mixkit] SFX per event, placed by its measured peak:

- a click on every image switch
- a key on every typed letter
- a soft landing on the stressed word
- whooshes
- impacts on the drop and the logo

Trim sounds around their useful peak rather than using the full stock file.

Fade the music on a dB curve under the end card.

Loudnorm to -14 LUFS.
</sound>

<build>
1. One HTML canvas. Every frame is a pure function of time inside seek(t), and every caption and cut reads the word table.

2. The glass: snapshot the canvas behind the shape, blur it about 14px for the body, draw a lightly blurred copy magnified about 1.06x in a 12px band along the edge, then add the milk, sheen, rim and shadow.

3. Render with Playwright at 60fps with 8 motion-blur subframes, then encode with ffmpeg.

4. Before you show me anything: a contact sheet of stills, a frame-diff scan for single-frame pops (only the 16th-note runs may jump), and the voice-over-music ratio for every phrase.
</build>

<gotchas>
A [warmly] opener comes out whispered and [excited] can sound fake.

A highlight box behind a word looks like a Windows text selection.

If a scene's camera restarts at 1.0 mid-handoff, the zoom snaps.

A 0.05s fade reads as a pop-in.
</gotchas>

<start>
Ask me for the inputs, write the script, send me 4 voice takes to pick, then show me 8 stills before the full render.
</start>
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `[DEFAULT PRODUCT NAME]` | Name of the product or brand | `HyperTrack` |
| `[DEFAULT ONE-LINE PITCH]` | Core value proposition | `Real-time geospatial intelligence for autonomous fleets` |
| `[DEFAULT FONT, e.g. Geist]` | Primary brand typeface | `Geist` |
| `[DEFAULT INK COLOUR, e.g. #111214]` | Primary text and element colour | `#111214` |
| `[DEFAULT ELEVENLABS VOICE + VOICE ID]` | Selected voice talent and ID | `Rachel (21m00Tcm4TlvDq8ikWAM)` |
| `[DEFAULT VOICE MODEL]` | Voice model version | `eleven_multilingual_v2` |
| `[DEFAULT ROYALTY-FREE TRACK]` | Track identifier or file | `Neon Horizons by Soundroll` |
| `[TRACK BPM]` | Beats per minute | `124` |
| `[DROP TIMESTAMP]` | Exact point where the musical drop hits | `00:07.740` |
| `[DURATION]` | Film length | `22 seconds` |
| `[ASPECT RATIO]` | Frame format | `square` |
| `[RESOLUTION]` | Export canvas resolution | `1440x1440` |
| `[FPS]` | Frame rate | `60fps` |
| `[VISUAL DIRECTION / BRAND FILM STYLE]` | Overall aesthetic treatment | `Tactile minimalism with frosted liquid glass controls` |
| `[PRODUCT-SPECIFIC CONTROLS]` | Key user controls to visualize | `Speed slider, waypoint selector, coordinate toggle` |
| `[PRODUCT'S PRIMARY INPUT CONTROL]` | Main UI element demonstrated at the drop | `Prompt input bar with glowing dispatch trigger` |
| `[NUMBER]` | Count of reference or input images | `4` |
| `[SFX SOURCE, default Mixkit]` | Sound effect asset library | `Mixkit` |

## 💡 Example

```text
<inputs>
Ask me for:

- my product or brand name
- a one-line pitch
- my logo
- [NUMBER] screenshots of the product
- [NUMBER]+ images of what the product creates, sells, enables, or represents
- brand colours
- brand font
- voice-generation credentials or preferred voice
- a royalty-free song with a clearly identifiable drop
- the song file
- the drop timestamp

Also ask for any product-specific inputs, outputs, controls, settings, or interactions that should appear in the film.

If I omit an input, use sensible defaults appropriate to the product rather than blocking the project.

Defaults:

Product name: [DEFAULT NAME]

Pitch: [DEFAULT PITCH]

Imagery source: [DEFAULT IMAGE SOURCE]

Typeface: [DEFAULT FONT]

Primary ink: [DEFAULT COLOUR]

Voice: [DEFAULT VOICE / MODEL]

Music: [DEFAULT TRACK / BPM / DROP TIMESTAMP]
</inputs>

<script>
Write a short launch-film voiceover of approximately [TARGET LENGTH / NUMBER OF LINES].

Map every line specifically to my product.

Use this narrative shape as a starting framework:

"This is [NAME].

A [CATEGORY] made for [CORE VALUE].

[PRIMARY ACTION / VERB] in [DISTINCTIVE CAPABILITY].

Give it [INPUT] — and it [PRODUCT MAGIC].

The more you use it, the [BENEFIT / IMPROVEMENT].

Control its [SETTING].

Its [SETTING].

Its [SETTING].

Every [OUTPUT] — exactly how you want it.

[NAME]. [CTA]."

Adapt this structure when the product requires a different narrative.

Do not force generic AI-product language onto a product where it does not fit.

Use emotional voice tags sparingly.

Reserve heightened delivery for the film's primary action or climax.

Keep quiet lines restrained.

The opening should normally be delivered plainly unless the brand requires otherwise.
</script>

<voice>
Generate [NUMBER] complete voice takes so I can compare delivery.

Keep each complete script in one natural read where possible.

If a single line is weak, regenerate only that line in multiple versions and splice the selected replacement into the chosen take rather than regenerating the entire performance.

Clean excessive pauses without making the delivery feel artificially rushed.

Normalize phrase loudness gently so the read feels coherent while retaining natural emphasis.

For accurate word timing, do not rely blindly on one whole-file transcription pass if timing precision is poor.

Where necessary:

1. identify meaningful pauses
2. split the performance into phrases or chunks
3. transcribe those chunks separately
4. align each chunk to its measured audio onset
5. build one authoritative word-timing table

That timing table becomes the source of truth for captions and synchronized visual events.
</voice>

<direction>
Create a [DURATION]-second [ASPECT RATIO] launch film at [RESOLUTION] and [FPS].

Visual direction:

[DESCRIBE BRAND / FILM AESTHETIC]

Use the real product, real outputs, real imagery, and real brand identity wherever possible.

Do not hide a weak concept behind decorative motion.

All captions should appear in synchronization with the spoken words.

If the brand uses translucent or glass controls, make them react convincingly to the scene behind them rather than behaving like flat semitransparent rectangles.

Where glass appears over a visually empty background, introduce subtle environmental colour, imagery, or light behind it so refraction and blur have something to affect.

Use typographic emphasis selectively.

A stressed word may receive:

[BRAND-SPECIFIC EMPHASIS TREATMENT]

but avoid turning every line into an effect.

Motion rules:

- maintain subtle continuous camera or composition movement unless stillness is intentional
- preserve camera continuity across scene handoffs
- avoid elements appearing with single-frame pops unless deliberately used for rhythmic cuts
- use fades or eased transitions of at least [MINIMUM TRANSITION TIME]
- synchronize rhythmic image changes to the music grid where appropriate
- land important scene changes on phrase boundaries
- align the music's major drop or climax with [KEY SCRIPT MOMENT]

Banned:

- [BANNED VISUAL DEVICE]
- [BANNED VISUAL DEVICE]
- [BANNED MOTION DEVICE]
- [BANNED STYLE]
- obvious templates
- effects that conflict with the brand
</direction>

<structure>
Build approximately [NUMBER] scenes around the voiceover.

Use this as a structural framework, not a mandatory visual template.

1. INTRODUCTION

Introduce [NAME] using [PRODUCT IMAGERY / BRAND MATERIAL].

Let the product name and category establish themselves clearly.

2. CORE VALUE

Demonstrate the primary value proposition using the strongest available product imagery.

3. PRIMARY ACTION / CLIMAX

Synchronize the film's strongest musical or visual moment with the product's main action.

Show:

[PRIMARY PRODUCT INTERACTION]

4. INPUT / UNDERSTANDING

Demonstrate what the user gives the product and how the product responds.

Use:

[REAL INPUT / WORKFLOW]

5. IMPROVEMENT / BENEFIT

Show the product becoming more useful, accurate, personalized, powerful, or valuable.

Use the actual product mechanism rather than inventing one.

6. CONTROL / SETTINGS

Reveal [2–4] meaningful controls, settings, or decisions.

Animate each one when it is referenced in the voiceover.

The visual result should respond to those controls.

7. OUTPUT / END CARD

Build toward a dense or memorable presentation of the product's outputs, customers, creations, or results.

Resolve that energy into the logo or product identity.

Show:

[CTA]

Hold the final identity long enough to read comfortably.

Replace generic prompt bars, sliders, result cards, dashboards, or controls with the product's real interaction model whenever possible.
</structure>

<sound>
Align the music so its primary drop or climax lands on:

[KEY SCRIPT LINE / EVENT]

Build the beat grid around that anchor.

Duck music intelligently under narration rather than globally turning the track down.

Prioritize vocal intelligibility in the speech-frequency range while retaining bass energy and high-frequency atmosphere where possible.

Target approximately [VOICE-OVER-MUSIC RELATIONSHIP] during spoken phrases.

Use sound effects only for meaningful events.

Possible event categories:

- image changes
- typed characters
- UI interactions
- transitions
- whooshes
- impacts
- climax/drop
- final logo resolve

Do not add a sound merely because something moves.

Trim effects around the useful transient or peak rather than dropping long stock files onto the timeline unchanged.

Fade the music naturally under the end card.

Target final loudness:

[TARGET LUFS]
</sound>

<build>
Prefer a deterministic programmatic rendering architecture.

1. Use [CANVAS / WEBGL / DOM / OTHER RENDERING SYSTEM] as appropriate.

2. Make every rendered frame derive from time through a deterministic function such as:

seek(t)

The frame at time `t` should be reproducible regardless of playback history.

3. Captions, scene transitions, and synchronized events should read from the authoritative timing data rather than using unrelated timers.

4. Implement any custom materials or effects explicitly rather than relying on screenshots of UI effects.

For example, a glass treatment may include:

- captured background
- blur
- localized magnification/refraction
- tint or milk
- highlight/sheens
- rim lighting
- shadow or spatial lift

5. Render frames through [PLAYWRIGHT / BROWSER AUTOMATION / RENDER ENGINE].

6. If needed, use motion-blur subframes rather than relying only on post-process blur.

7. Encode the final sequence with [FFMPEG / OTHER ENCODER].

8. Preserve deterministic timing between:

- animation
- captions
- voice
- music
- sound effects
</build>

<qa>
Before showing me the final render:

1. Generate a contact sheet containing approximately [NUMBER] representative frames from across the film.

2. Inspect those frames for:

- weak composition
- inconsistent typography
- accidental clipping
- broken image crops
- bad glass/refraction
- inconsistent spacing
- visual repetition
- brand inconsistency

3. Run a frame-difference scan to identify unexpected one-frame jumps or flashes.

4. Distinguish intentional rhythmic cuts from accidental pops.

5. Check voice-to-music intelligibility for every spoken phrase.

6. Verify that major visual events align with their intended spoken words.

7. Verify that scene handoffs do not reset camera scale, position, lighting, or other state unintentionally.

8. Inspect the opening frame, climax frame, and final frame individually.

Do not treat a successful render or encode as proof that the film is visually finished.
</qa>

<gotchas>
Known failure modes:

- emotional voice tags can easily become theatrical, whispered, or artificial
- excessive typographic highlighting can look like text selection rather than art direction
- restarting camera state between scenes creates visible snapping
- extremely short fades read as accidental pop-ins
- decorative glass over featureless white has nothing meaningful to refract
- beat synchronization is not automatically good motion design
- too many sound effects make the film feel like a UI demo rather than a launch film
- stock interface elements should not replace the product's actual interaction model
- one transcription pass may not provide sufficiently accurate word timing
- technically correct output can still contain bad individual frames

Add project-specific failure modes discovered during iteration to this section rather than repeatedly rediscovering them.
</gotchas>

<start>
Ask me for the required inputs first.

Then:

1. write the proposed script
2. generate or prepare [NUMBER] voice takes
3. let me choose the preferred performance
4. resolve any weak lines
5. establish the timing table
6. show me approximately [NUMBER] representative stills
7. address obvious visual problems
8. render the complete film

Do not jump directly to the final render before the script, voice, timing, and representative stills have been reviewed.
</start>
```
