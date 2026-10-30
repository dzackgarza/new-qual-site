---
schema: qual/card@1
id: P-MMAQ-FLFHFN7LEF
kind: problem
title: '$\int_0^\infty \frac{\cos x}{(1+x^2)^2}\,dx$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Integrals
  - Residues
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Complex Analysis (1) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMCA1, whose solution repeats this residue computation."
---

::: {.problem}
Use residues to compute the integral
$$
\int_{0}^{\infty} \frac{\cos x}{(x^2+1)^2}\,dx.
$$
:::

::: {.solution}

Let $f(z)=\dfrac{e^{iz}}{(z^2+1)^2}$, and for $R>1$ let $\Gamma_R$ be the segment $[-R,R]$ followed by the upper semicircle $C_R=\{Re^{it}:0\le t\le\pi\}$.

::: pf

::: {.pf-step #even}

$$
\int_0^\infty\frac{\cos x}{(x^2+1)^2}\,dx=\frac12\lim_{R\to\infty}\int_{-R}^{R}f(x)\,dx.
$$

::: pf-proof

The function $\frac{\cos x}{(x^2+1)^2}$ is even and $\frac{\sin x}{(x^2+1)^2}$ is odd, and both are integrable on $\RR$.

:::

:::

::: {.pf-step #res}

$\operatorname{Res}_{z=i}f=\dfrac{1}{2ie}$.

::: pf-proof

The only pole of $f$ in the upper half-plane is the double pole $i$. With $h(z)=e^{iz}(z+i)^{-2}$,
$$
h'(z)=\frac{e^{iz}\bigl(i(z+i)-2\bigr)}{(z+i)^3},
\qquad
h'(i)=\frac{e^{-1}(-4)}{(2i)^3}=\frac{-4e^{-1}}{-8i}=\frac{1}{2ie}.
$$

:::

:::

::: {.pf-step #arc}

$\displaystyle\lim_{R\to\infty}\int_{C_R}f(z)\,dz=0$.

::: pf-proof

For $z\in C_R$, $\abs{e^{iz}}=e^{-\operatorname{Im}z}\le1$ and $\abs{z^2+1}\ge R^2-1$. So the integral has modulus at most $\pi R/(R^2-1)^2$, which tends to $0$.

:::

:::

::: {.pf-step #val}

$$
\boxed{\int_0^\infty\frac{\cos x}{(x^2+1)^2}\,dx=\frac{\pi}{2e}}
$$

::: pf-proof

By the residue theorem and Step [](#res){.pf-ref}, $\int_{\Gamma_R}f=2\pi i\cdot\frac{1}{2ie}=\frac{\pi}{e}$ for every $R>1$. Let $R\to\infty$ and apply Steps [](#arc){.pf-ref} and [](#even){.pf-ref}.

:::

:::

::: pf-qed

Step [](#val){.pf-ref} is the requested value.

:::

:::

:::
