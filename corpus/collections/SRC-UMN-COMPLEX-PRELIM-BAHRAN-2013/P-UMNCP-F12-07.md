---
schema: qual/card@1
id: P-UMNCP-F12-07
kind: problem
title: A positive-real-part function has a removable puncture
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2012, 7 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Suppose $f$ is analytic on the punctured unit disk $\DD\setminus\{0\}$ and
$$
\operatorname{Re} f(z)>0.
$$
Prove that $f$ has a removable singularity at $0$.
:::

::: {.solution}

Define the Cayley transform
$$
g(z)
\coloneqq
\frac{f(z)-1}{f(z)+1}.
$$

::: pf

::: {.pf-step #s1-1}

The denominator $f(z)+1$ never vanishes on $\DD\setminus\{0\}$.


::: pf-proof

If
$$
f(z)+1=0,
$$
then
$$
f(z)=-1,
$$
whose real part is $-1$, contradicting
$$
\operatorname{Re}f(z)>0.
$$

:::

:::

::: {.pf-step #s1-2}

The function $g$ is holomorphic on $\DD\setminus\{0\}$ and satisfies
$$
\boxed{|g(z)|<1}.
$$


::: pf-proof

Holomorphicity follows from step [](#s1-1){.pf-ref}. Write
$$
w=f(z).
$$
Then
$$
\operatorname{Re}w>0.
$$
Compute
$$
|w+1|^2-|w-1|^2
=
4\operatorname{Re}w
>0.
$$
Hence
$$
|w-1|<|w+1|,
$$
so
$$
\left|
\frac{w-1}{w+1}
\right|
<1.
$$
Thus $|g(z)|<1$.

:::

:::

::: pf-step

The singularity of $g$ at $0$ is removable.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
|g(z)|<1
$$
throughout the punctured disk. Thus $g$ is bounded near $0$. Riemann's removable-singularity theorem therefore gives a holomorphic extension
$$
\widetilde g:\DD\to\CC.
$$

:::

:::

::: {.pf-step #s1-4}

The extended value satisfies
$$
\boxed{|\widetilde g(0)|<1}.
$$


::: pf-proof

Continuity of $\widetilde g$ and step [](#s1-2){.pf-ref} give
$$
|\widetilde g(0)|\le1.
$$
Suppose equality held. Then $|\widetilde g|$ would attain its maximum value $1$ at the interior point $0$. By the maximum-modulus principle, $\widetilde g$ would be constant on the connected disk.

That constant would have modulus $1$, contradicting
$$
|g(z)|<1
$$
for every
$$
z\ne0.
$$
Hence
$$
|\widetilde g(0)|<1.
$$

:::

:::

::: {.pf-step #s1-5}

The function
$$
\widetilde f(z)
\coloneqq
\frac{1+\widetilde g(z)}
{1-\widetilde g(z)}
$$
is holomorphic in a neighborhood of $0$.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\widetilde g(0)\ne1.
$$
By continuity, after shrinking to a neighborhood of $0$ one has
$$
1-\widetilde g(z)\ne0.
$$
Thus the displayed quotient is holomorphic there.

:::

:::

::: {.pf-step #s1-6}

On the punctured disk,
$$
\widetilde f=f.
$$


::: pf-proof

For $z\ne0$,
$$
\widetilde g(z)=g(z)
=
\frac{f(z)-1}{f(z)+1}.
$$
Solving this identity for $f(z)$ gives
$$
f(z)
=
\frac{1+g(z)}
{1-g(z)}
=
\widetilde f(z).
$$

:::

:::

::: {.pf-step #s1-7}

Therefore the singularity of $f$ at $0$ is removable.


::: pf-proof

Step [](#s1-5){.pf-ref} gives a holomorphic function near $0$, and step [](#s1-6){.pf-ref} shows that it agrees with $f$ away from $0$. Hence it is a holomorphic extension of $f$ across the puncture.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
