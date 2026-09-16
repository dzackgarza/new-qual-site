---
schema: qual/card@1
id: P-FIOQC
kind: problem
title: Simple zeros of $\sin(\pi z)$ at the integers, and $\operatorname{Res}_{z=n}\frac{1}{\sin(\pi
  z)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Residues
  - Trigonometry
  - Poles
relations: []
review: draft
---

::: {.problem}
Use the following formula to show that the complex zeros of $\sin(\pi z)$ are exactly the integers, and they are each of order 1:
\[
\sin \pi z=\frac{e^{i \pi z}-e^{-i \pi z}}{2 i}
.\]

Calculate the residue of ${1\over \sin(\pi z)}$ at $z=n\in \ZZ$.
:::

::: {.solution}
From
\[
\sin(\pi z)=\frac{e^{i\pi z}-e^{-i\pi z}}{2i},
\]
we have $\sin(\pi z)=0$ exactly when
\[
e^{2\pi i z}=1.
\]
Writing $z=x+iy$, the modulus of the left side is $e^{-2\pi y}$, so $y=0$;
then $e^{2\pi i x}=1$, hence $x\in\mathbb Z$. Thus the zeros are exactly the
integers.

Moreover
\[
\frac{d}{dz}\sin(\pi z)=\pi\cos(\pi z),
\]
and at $z=n$ this equals $\pi(-1)^n\ne0$, so every zero is simple. Therefore
$1/\sin(\pi z)$ has a simple pole at $n$ with residue
\[
\boxed{
\operatorname{Res}_{z=n}\frac1{\sin(\pi z)}
=\frac1{\pi\cos(\pi n)}
=\frac{(-1)^n}{\pi}.}
\]
:::
