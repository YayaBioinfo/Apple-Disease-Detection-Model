# 🍎 Apple Disease Detection Expert System

A simple rule-based expert system for detecting apple tree diseases through symptom-based diagnostic questions, built using Python.

---

## Description

This program helps users identify possible diseases in apple trees based on observed symptoms on leaves, stems, and fruit. After diagnosis, the program provides disease control recommendations and additional information about the detected disease.

---

## Detectable Diseases

| Code | Disease | Causative Agent | Affected Part |
|------|---------|-----------------|---------------|
| `LD` | Leaf Blight (*Marssonina coronaria* J.J. Davis) | Fungus | Leaves |
| `CC` | Canker (*Botryosphaeria ribis* Gross.) | Fungus | Stem and fruit |
| `U` | Undetected | — | — |

---

## Diagnostic Flow

```
Input user name
       │
       ▼
Changes on leaves?
  ├── Yes → leaf drop / black spots / white patches → LD
  └── No  → continue
       │
       ▼
Changes on stem?
  ├── Yes → stem rotting / oozing liquid → CC
  └── No  → continue
       │
       ▼
Changes on fruit?
  ├── Yes → fruit browning / rotting → CC
  └── No  → U (undetected)
       │
       ▼
Diagnosis result + control recommendation
       │
       ▼
Additional disease information (optional)
       │
       ▼
References (optional) + consultation timestamp
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## How to Run

```bash
python apple_disease_detector.py
```

The program runs entirely in the terminal interactively. Users simply answer each question with `yes` or `no`.

---

## Example Output

```
================================================================================
|          Welcome to the Apple Tree Disease Detection Program                 |
================================================================================
Please enter your identity
Name: Yaya

...

Hello, Yaya. The examination has detected that the apple tree is infected with Leaf Blight.

To control Leaf Blight, remove and burn the affected parts and apply fungicide.

Consultation conducted on: Thu May 14 10:30:00 2026
```

---

## Reference

Sastrahidayat, I. R. & Djauhari, S. (2013). *Penyakit dan Hama Apel serta Cara Pengendaliannya*. Brawijaya Press. Malang.

---

## Author

Program created by **Yaya**.
