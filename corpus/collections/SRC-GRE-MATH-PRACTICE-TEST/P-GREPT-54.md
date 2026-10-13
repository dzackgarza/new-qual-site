---
schema: qual/card@1
id: P-GREPT-54
kind: problem
title: "Contour integral of $\\cos z-z\\cos(1/z)$ over $\\abs{z}=\\pi$"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 54 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $C$ is the circle in the complex plane whose equation is $\abs{z} = \pi$, oriented counterclockwise, find the value of the integral

$$\oint_{C} \left( \cos z - z \cos \frac{1}{z} \right) dz$$

(A) $-2\pi i$
(B) $-\pi i$
(C) $0$
(D) $\pi i$
(E) $2\pi i$
:::

::: {.solution}
<1>1. The Laurent expansion of the integrand about $0$ has residue
$$
\frac12.
$$

::: {.proof}
Using the cosine series,
$$
\cos\frac1z
=1-\frac1{2!z^2}+\frac1{4!z^4}-\cdots,
$$
so
$$
-z\cos\frac1z
=-z+\frac1{2z}-\frac1{24z^3}+\cdots.
$$
The function $\cos z$ is entire and its Taylor series contains no negative
powers. Hence the coefficient of $z^{-1}$ in
$\cos z-z\cos(1/z)$ is $1/2$.
:::

<1>2. The only singularity of the integrand inside $C$ is $z=0$.

::: {.proof}
The term $\cos z$ is entire, while $z\cos(1/z)$ is holomorphic on
$\CC\setminus\{0\}$. Since the circle $|z|=\pi$ encloses the origin, $0$ is
the only enclosed singularity.
:::

<1>3. Therefore
$$
\oint_C\left(\cos z-z\cos\frac1z\right)dz
=\boxed{\pi i},
$$
so the answer is (D).

::: {.proof}
By the residue theorem and steps <1>1--<1>2,
$$
\oint_C\left(\cos z-z\cos\frac1z\right)dz
=2\pi i\left(\frac12\right)
=\pi i.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required contour integral.
:::
:::
