---
schema: qual/card@1
id: P-WESCA15-1
kind: problem
title: 'Classify three isolated singularities'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Classify each indicated isolated singularity as removable, a pole, or essential; for a pole give its order:

1. $\displaystyle \frac{(e^z-1)^3}{z^6}$ at $z=0$;

2. $\displaystyle \frac{\sin z}{z^2-\pi^2}$ at $z=\pi$;

3. $\displaystyle \frac{\cos(1/z)}{z^3}$ at $z=0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The singularity of
$$
f(z)=\frac{(e^z-1)^3}{z^6}
$$
at $z=0$ is a pole of order $3$.


::: pf-proof

The function
$$
\phi(z)=\frac{e^z-1}{z}
$$
for $z\ne0$ extends holomorphically to $z=0$ by setting
$$
\phi(0)=1,
$$
because
$$
e^z-1=z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots.
$$
Thus
$$
e^z-1=z\phi(z),
\qquad
\phi(0)=1\ne0.
$$
Hence
$$
f(z)
=\frac{z^3\phi(z)^3}{z^6}
=\frac{\phi(z)^3}{z^3}.
$$
The numerator is holomorphic and nonzero at $0$, so $f$ has a pole of order $3$ there.

:::

:::

::: {.pf-step #s1-2}

The singularity of
$$
g(z)=\frac{\sin z}{z^2-\pi^2}
$$
at $z=\pi$ is removable.


::: pf-proof

Factor the denominator:
$$
z^2-\pi^2=(z-\pi)(z+\pi).
$$
Since $\sin\pi=0$, the quotient
$$
\psi(z)=\frac{\sin z}{z-\pi}
$$
for $z\ne\pi$ extends holomorphically to $z=\pi$, with
$$
\psi(\pi)=\cos\pi=-1.
$$
Therefore, near $\pi$,
$$
g(z)=\frac{\psi(z)}{z+\pi},
$$
and the denominator is nonzero at $z=\pi$. Hence $g$ extends holomorphically across $\pi$, with value
$$
g(\pi)=-\frac1{2\pi}.
$$
Thus the singularity is removable.

:::

:::

::: {.pf-step #s1-3}

The singularity of
$$
h(z)=\frac{\cos(1/z)}{z^3}
$$
at $z=0$ is essential.


::: pf-proof

For $z\ne0$, the Laurent expansion is
$$
\cos(1/z)
=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}z^{-2k}.
$$
Hence
$$
h(z)
=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}z^{-(2k+3)}.
$$
The principal part contains infinitely many nonzero negative-power terms. Therefore the singularity is neither removable nor a pole of finite order, so it is essential.

:::

:::

::: {.pf-step #s1-4}

Therefore the classifications are
$$
\boxed{
\begin{array}{c|c}
\text{function}&\text{singularity}\\ \hline
(e^z-1)^3/z^6&\text{pole of order }3\\
\sin z/(z^2-\pi^2)&\text{removable at }\pi\\
\cos(1/z)/z^3&\text{essential at }0
\end{array}}
$$


::: pf-proof

This is exactly the combination of steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives all three requested classifications, including the order of the only pole.

:::

:::

:::
