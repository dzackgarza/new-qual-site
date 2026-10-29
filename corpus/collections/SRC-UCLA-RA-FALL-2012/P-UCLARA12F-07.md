---
schema: qual/card@1
id: P-UCLARA12F-07
kind: problem
title: Boundary derivative for a disc self-map
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f$ be holomorphic on $\CC$ and suppose that $f(0)=0$, $f(1)=1$, and $f(\mathbb D)\subseteq\mathbb D$, where $\mathbb D$ is the unit disc.
Show that

(a) $f'(1)\in\RR$;

(b) $f'(1)\ge1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $z\in\mathbb D$,
$$
|f(z)|\le |z|.
$$


::: pf-proof

The map $f$ is holomorphic on $\mathbb D$, satisfies $f(0)=0$, and maps $\mathbb D$ into itself. Schwarz's lemma therefore gives the estimate.

:::

:::

::: {.pf-step #s1-2}

For every $\zeta$ on the unit circle,
$$
|f(\zeta)|\le1.
$$


::: pf-proof

Fix $|\zeta|=1$. For $0<r<1$, step [](#s1-1){.pf-ref} gives
$$
|f(r\zeta)|\le r.
$$
Since $f$ is entire, it is continuous at $\zeta$. Letting $r\uparrow1$ yields $|f(\zeta)|\le1$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{f'(1)\in\RR}.
$$


::: pf-proof

Define
$$
\phi(t)\coloneqq |f(e^{it})|^2.
$$
By step [](#s1-2){.pf-ref}, $\phi(t)\le1$ for all real $t$, while
$$
\phi(0)=|f(1)|^2=1.
$$
Thus $t=0$ is a maximum of the differentiable real-valued function $\phi$, so $\phi'(0)=0$. Differentiating gives
$$
\begin{aligned}
0
=\phi'(0)
&=2\operatorname{Re}\!\left(i f'(1)\overline{f(1)}\right)\\
&=2\operatorname{Re}(i f'(1)).
\end{aligned}
$$
Since $f(1)=1$, this says
$$
\operatorname{Im}f'(1)=0.
$$
Hence $f'(1)$ is real.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\operatorname{Re}f'(1)\ge1.
$$


::: pf-proof

For $0<r<1$, step [](#s1-1){.pf-ref} gives
$$
|f(r)|\le r.
$$
Set $h=1-r>0$. Since $f$ is holomorphic at $1$,
$$
f(1-h)=1-h f'(1)+o(h).
$$
Therefore
$$
|f(1-h)|^2
=1-2h\operatorname{Re}f'(1)+o(h).
$$
On the other hand,
$$
|f(1-h)|^2\le(1-h)^2=1-2h+o(h).
$$
Subtract $1$, divide by $-2h<0$, and let $h\downarrow0$. The inequality reverses under division by the negative quantity and gives
$$
\operatorname{Re}f'(1)\ge1.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{f'(1)\ge1}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, $f'(1)$ is real. Step [](#s1-4){.pf-ref} then gives the stated inequality.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
