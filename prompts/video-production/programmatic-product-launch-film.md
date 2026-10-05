---
title: "Programmatic Product Launch Film Director"
category: "video-production"
tags: ["video-production", "launch-film", "motion-design", "programmatic-video", "ffmpeg", "voiceover", "scriptwriting", "art-direction"]
description: "End-to-end director pipeline for writing, voicing, scoring, choreographing, programmatically rendering, and QAing cinematic product launch films."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o"]
version: "1.0"
---

# Programmatic Product Launch Film Director

## 🎯 Overview
An end-to-end framework and autonomous director pipeline for creating high-caliber, cinematic product launch videos. Controls the complete production lifecycle: input intake, modular voiceover scripting, multi-take voice generation and chunk-aligned word timing, visual art direction, music drop synchronization, deterministic programmatic rendering (`seek(t)`), and rigorous contact-sheet QA.

## 📋 Prompt
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

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `[NUMBER]` | Counts for screenshots, scenes, voice takes, or QA stills | `5` screenshots, `3` voice takes, `12` QA stills |
| `[DEFAULT ...]` | Sensible fallback values if user input is omitted | `HyperTrack`, `Geospatial AI for fleets`, `Space Grotesk`, `#0A84FF` |
| `[TARGET LENGTH / NUMBER OF LINES]` | Length of narration script | `45 seconds / 12 lines` |
| `[DURATION]`, `[ASPECT RATIO]`, `[RESOLUTION]`, `[FPS]` | Video output specifications | `30s`, `16:9`, `3840x2160 (4K)`, `60fps` |
| `[DESCRIBE BRAND / FILM AESTHETIC]` | Visual style guidelines | `Dark technical minimalism with high-contrast amber accents and tactile glass cards` |
| `[BANNED VISUAL / MOTION DEVICE]` | Explicitly prohibited clichés | `Spinning 3D globes`, `Purple gradient mesh`, `Fake terminal text typing` |
| `[KEY SCRIPT LINE / EVENT]` | Narrative anchor for music drop | `When the voiceover says: 'Every route — instantly solved'` |
| `[RENDERING & ENCODING ENGINES]` | Tooling stack | `WebGL / Canvas`, `Playwright headless`, `FFmpeg with libx264/AAC` |

## 💡 Example
### Input
```text
Product: FlowCanvas — collaborative canvas for AI pipeline engineering.
Duration: 30 seconds, 16:9, 4K 60fps.
Music Drop: 00:14.200 on "Assemble models at the speed of thought".
Voice: Deep, measured, confident female voice (ElevenLabs George / Rachel).
```

### Expected Output
The director asks for asset links/defaults, drafts a tailored 10-line voiceover script, produces 3 voice candidate takes, generates word-level timestamp tables, scripts deterministic `seek(t)` canvas scenes, coordinates ducking and sound design around the 14.2s drop, and generates a 12-frame contact sheet before final FFmpeg encoding.
