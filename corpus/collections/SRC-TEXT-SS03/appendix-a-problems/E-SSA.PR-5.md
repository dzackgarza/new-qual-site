---
schema: qual/card@1
id: E-SSA.PR-5
kind: problem
title: "The exact formula for $p(n)$: the transformation at every rational point"
classification:
  areas:
  - complex-analysis
  topics:
  - Partitions
  - Modular Forms
  - Asymptotics
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 5,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
---

::: {.exercise}
The one shortcoming in our derivation of the asymptotic formula for $p(n)$ arose from the fact that while $f_1(z)=\frac{z}{i}e^{\frac{\pi i}{12z}}e^{\frac{\pi iz}{12}}$ is a good approximation to the generating function $f(z)$ near $z=0$, this fails near other points on the real axis, since $f_1$ is regular there, but $f$ is not.

However, using the transformation law (24) and the identity $f(z+1)=f(z)$, one can derive the following generalization of (24): whenever $p/q$ is a rational number in lowest form (so $p$ and $q$ are relatively prime) then
$$
f\Bigl(z-\frac{p}{q}\Bigr)=\omega_{p/q}\Bigl(\frac{zq}{i}\Bigr)^{1/2}e^{\frac{\pi i}{12zq^2}}e^{-\frac{\pi iz}{12}}f\Bigl(-\frac{1}{zq^2}-\frac{p'}{q}\Bigr),
$$
where $pp'\equiv1 \pmod q$. Here $\omega_{p/q}$ is an appropriate $24$th root of unity. This formula leads to an analogous $f_{p/q}$, approximating $f$ at $z=p/q$.

From this one can obtain for each $p/q$ a contribution of the form
$$
c_{p/q}\frac{1}{2\pi\sqrt{2}}\frac{d}{dn}\Bigl[\frac{e^{\frac{K}{q}(n-\frac{1}{24})^{1/2}}}{(n-\frac{1}{24})^{1/2}}\Bigr]
$$
to the asymptotic formula for $p(n)$. When suitably modified, the resulting series, summed over all proper fractions $p/q$ in $[0,1)$, actually converges and gives an exact formula for $p(n)$.
:::

