---
schema: qual/card@1
id: P-GRECH7-46
kind: problem
title: Solutions of $\cos z=3$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 46 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The five choices are garbled identically in both extractions and no longer differ as printed; the book's Chapter 8 solution gives z = 2k pi - i log(3 +/- 2 sqrt 2).
---

::: {.problem}
For what complex number $z$ does $\cos z=3$?

(A) $i \log \left(3 \pm 2\sqrt{2i}\right) + 2k\pi$, for any $k \in \mathbb{Z}$
(B) $2k\pi - i \log \left(3 \pm 2\sqrt{2i}\right)$, for any $k \in \mathbb{Z}$
(C) $2k\pi - i \log \left(3 \pm 2\sqrt{2i}\right)$, for any $k \in \mathbb{Z}$
(D) $i \log \left(3 \pm 2\sqrt{2i}\right) + 2k\pi$, for any $k \in \mathbb{Z}$
(E) $i \log \left(3 \pm 2\sqrt{2i}\right) + 2k\pi$, for any $k \in \mathbb{Z}$
:::

::: {.remark}
As printed in the source, choices (B) and (C) coincide, as do (A), (D) and (E). From $e^{iz}+e^{-iz}=6$, one gets $e^{iz}=3\pm2\sqrt2$, so the solutions are $z=2k\pi-i\log(3\pm2\sqrt2)$ for $k\in\mathbb{Z}$.
:::
