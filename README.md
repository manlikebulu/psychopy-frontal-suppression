# README: Frontal Alpha Suppression During Selective Attention Tasks

## Overview

This project investigates frontal alpha suppression as a neural correlate of selective attention using EEG recordings. The study employs two cognitive paradigms [Stroop Task and Oddball Task] designed and implemented in PsychoPy, with EEG data acquired using the Muse headband and synchronized via Lab Streaming Layer (LSL).

The primary focus is on frontal electrode activity (AF7 and AF8) to assess changes in alpha-band power during attentional demand.

---

## Objectives

### Primary Objective

To assess whether alpha-band power decreases (alpha suppression) at frontal sites during cognitively demanding tasks.

### Secondary Objectives

* Compare neural responses between congruent and incongruent Stroop trials
* Evaluate attentional responses to rare stimuli in the Oddball paradigm
* Validate the feasibility of low-channel EEG systems for cognitive neuroscience research

---

## Experimental Tasks

### 1. Stroop Task

Participants respond to the ink color of color words:

* Conditions: Congruent and Incongruent
* Total Trials: 120 (60 congruent, 60 incongruent)
* Response Keys:

  * R = Red
  * B = Blue
  * G = Green
  * Y = Yellow

### 2. Oddball Task

Participants respond to infrequent target stimuli among frequent standard stimuli.

---

## Hardware and Software

### EEG Device

* Muse EEG Headband
* Channels: AF7, AF8, TP9, TP10

### Software

* PsychoPy (task presentation)
* Lab Streaming Layer (LSL) for synchronization
* LabRecorder (data acquisition)
* Python (data analysis)
* MNE (EEG processing)

---

## EEG Markers (LSL)

Markers are sent from PsychoPy to synchronize behavioral events with EEG data.

| Event             | Marker Code |
| ----------------- | ----------- |
| Congruent Trial   | 1           |
| Incongruent Trial | 2           |
| Response          | 10          |
| Practice Start    | 99          |
| Main Task Start   | 100         |

Markers are sent at stimulus onset to ensure accurate temporal alignment.

---

## File Structure

* `stroop_conditions.xlsx` → Main Stroop trials (120 trials)
* `stroop_practice.xlsx` → Practice trials (4 trials)
* PsychoPy `.psyexp` file → Experiment design
* EEG recordings → `.xdf` files (via LabRecorder)

---

## Experimental Procedure

1. Participant setup and consent
2. Muse EEG placement and signal check
3. Baseline recording (optional)
4. Practice trials
5. Main Stroop task
6. Oddball task
7. Debriefing

---

## Data Analysis Overview

### Preprocessing

* Bandpass filtering (1–40 Hz)
* Artifact removal (movement, blinks)
* Channel inspection

### Epoching

* Segment EEG data based on LSL markers
* Separate epochs:

  * Congruent trials
  * Incongruent trials

### Feature Extraction

* Alpha band (8–12 Hz) power
* Focus on AF7 and AF8

### Statistical Analysis

* Within-subject comparison:

  * Congruent vs Incongruent
* Expected outcome:

  * Reduced alpha power during incongruent trials

---

## Key Hypothesis

Frontal alpha power will decrease during high attentional demand conditions (incongruent Stroop trials), reflecting increased cortical engagement.

---

## Limitations

* Low spatial resolution (4-channel EEG)
* Susceptibility to motion artifacts
* Limited coverage of posterior brain regions

---

## Significance

This study demonstrates that meaningful cognitive neuroscience insights can be obtained using portable EEG systems, supporting scalable and accessible research methodologies.

---

## Notes for Replication

* Ensure stable Muse connection before recording
* Confirm LSL stream is active before starting tasks
* Use consistent lighting and minimal distractions
* Maintain fixed viewing distance for all participants

---

## Contact / Lab Use

This experiment is designed for research and training purposes in cognitive neuroscience and human attention studies.

---