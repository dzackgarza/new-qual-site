---
schema: qual/card@1
id: P-NKCDN
kind: problem
title: "Solution: $u_1 = \\cos (x)\u200b$, $v_1 = e^x\u200b$, $du_1 = - \\sin (x) ~dx\u200b$, $dv_1 = e^x ~dx\u200b$"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - integration-by-parts
  - trigonometry
relations: []
review: draft
---

::: problem
- **Solution:** $u_1 = \cos (x)​$, $v_1 = e^x​$, $du_1 = - \sin (x) ~dx​$, $dv_1 = e^x ~dx​$

- **Solution:** $ u_2 = \sin (x)$, $v_2 = e^x$, $du_2 = \cos (x) ~dx$, $dv_2 = e^x ~dx$

- **Solution:** $e^x \cos (x) - \int - e^x \sin (x) ~dx = e^x \cos (x) + (e^x \sin (x) - \int e^x \cos (x) ~dx)$

8. $\displaystyle \int \sin(\ln(x)) ~dx = \color {blue} {\frac {1}{2} x (\sin (\ln (x)) - \cos (\ln (x)))}​$

- **Solution:** $u_1 = \sin (\ln (x))​$, $v_1 = x​$, $du_1 = \frac {\cos (\ln (x))}{x}​$, $dv_1 = dx​$

- **Solution:** $u_2 = \cos (\ln (x))$, $v_2 = x$, $du_2 = \frac {- \sin (\ln (x))}{x}$, $dv_2 = dx$

- **Solution:** $x \sin (\ln (x)) - \int \frac {\cos (\ln (x))}{x} \cdot x ~dx = x \sin (\ln (x)) - (x \cos (\ln (x)) - \int \frac {- \sin (\ln (x))}{x} \cdot x ~dx)​$
:::
