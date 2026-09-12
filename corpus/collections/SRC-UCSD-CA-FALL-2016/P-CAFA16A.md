---
schema: qual/card@1
id: P-CAFA16A
kind: problem
title: "An entire function with f(z) → ∞ must be a polynomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Prove that if $f$ is an entire function such that $\lim_{z \to \infty} f(z) = \infty$, then $f$ must be a polynomial.
:::

::: solution
Set $g(w)=f(1/w)$ on a punctured neighborhood of $0$. The hypothesis says
\[
|g(w)|\to\infty\qquad (w\to0).
\]
Hence $1/g(w)\to0$, so $1/g$ has a removable singularity at $0$, with value $0$ there. Therefore $g$ has a pole at $0$.

Equivalently, $f$ has a pole at infinity. Thus the Laurent expansion of $f$ at infinity has only finitely many positive powers of $z$, so the Taylor series of the entire function $f$ terminates. Hence $f$ is a polynomial.
:::
