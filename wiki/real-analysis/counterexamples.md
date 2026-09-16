---
title: Counterexamples
order: 8
topics:
- Counterexamples
---

# Counterexamples

Each example below refutes the statement in its title.

## Convergence and integration

::: {.example title="The limit of the integrals need not be the integral of the limit"}
On $\RR$ with Lebesgue measure, each of the following sequences converges pointwise to $0$ while $\int f_n = 1$ for every $n$:

- $f_n \coloneqq n\chi_{[0,1/n]}$, whose mass concentrates near $0$;

- $f_n \coloneqq \frac1n\chi_{[0,n]}$, which is uniformly bounded by $1$, so the bounded convergence theorem requires a space of finite measure;

- $f_n \coloneqq \chi_{[n,n+1]}$, whose mass escapes to infinity.

In each case $\sup_n f_n$ is not integrable, so no integrable function dominates the sequence, and the dominated convergence theorem does not apply.
Each sequence also converges almost everywhere without converging in $L^1$.

:::

::: {.example title="Convergence in $L^p$ does not imply almost-everywhere convergence"}
For $n = 2^k + j$ with $0\leq j < 2^k$, let $f_n \coloneqq \chi_{[j2^{-k},\,(j+1)2^{-k}]}$ on $[0,1]$ (the typewriter sequence).
Then $\norm{f_n}_p = 2^{-k/p}\to 0$ for every $p<\infty$, but for every $x\in[0,1]$ the sequence $f_n(x)$ takes the value $1$ infinitely often and the value $0$ infinitely often, so it converges at no point.
Every sequence converging in $L^p$ has a subsequence converging almost everywhere; here $f_{2^k}=\chi_{[0,2^{-k}]}\to 0$ on $(0,1]$.

:::

## Measure

::: {.example title="A subset of $\RR$ that is not Lebesgue measurable"}
The Vitali set, a set of representatives of $\RR/\QQ$ in $[0,1]$ chosen using the axiom of choice, is not Lebesgue measurable.

:::

::: {.example title="A Lebesgue measurable set that is not Borel"}
The Lebesgue $\sigma$-algebra is the completion of the Borel $\sigma$-algebra.
Let $c$ be the Cantor function and $\psi(x) \coloneqq x + c(x)$, a homeomorphism $[0,1]\to[0,2]$ that maps the Cantor set $C$ onto a set of measure $1$.
Choose a non-measurable $A\subseteq\psi(C)$ and put $B\coloneqq\psi^{-1}(A)\subseteq C$.
Then $B$ is Lebesgue measurable, being a subset of the null set $C$, but $B$ is not Borel, since $\psi(B)=A$ is the preimage of $B$ under the continuous map $\psi^{-1}$ and preimages of Borel sets under continuous maps are Borel.

:::

::: {.example title="A composition of Lebesgue measurable functions need not be measurable"}
With $\psi$, $A$, and $B$ as in the previous example, $\chi_B$ is Lebesgue measurable and $\psi^{-1}\colon[0,2]\to[0,1]$ is continuous, but $\chi_B\circ\psi^{-1} = \chi_A$ is not Lebesgue measurable.
If $g$ is continuous and $f$ is Lebesgue measurable, then $g\circ f$ is Lebesgue measurable.

:::

::: {.example title="A set of positive measure need not contain an interval"}
A fat Cantor set, obtained from $[0,1]$ by removing at stage $n\geq1$ an open middle interval of length $4^{-n}$ from each of the $2^{n-1}$ remaining closed intervals, is closed, has measure $1/2$, and contains no interval.

:::

## $L^p$ spaces

::: {.example title="Neither of $L^1(\RR)$ and $L^2(\RR)$ contains the other"}
The function $x^{-1/2}\chi_{(0,1)}$ is in $L^1(\RR)$ and not in $L^2(\RR)$, and $x^{-1}\chi_{(1,\infty)}$ is in $L^2(\RR)$ and not in $L^1(\RR)$.
On a space of finite measure, $L^q\subseteq L^p$ for $p<q$.

:::

::: {.example title="The dual of $L^\infty$ is not $L^1$"}
The map $L^1([0,1])\to (L^\infty([0,1]))^*$, $g\mapsto\qty{f\mapsto\int fg}$, is not surjective: a Hahn--Banach extension $\varphi$ of $f\mapsto f(0)$ from $C([0,1])\subseteq L^\infty([0,1])$ is not of this form, since continuous $f_n$ with $0\leq f_n\leq 1$, $f_n(0)=1$, and $f_n\to0$ on $(0,1]$ give $\varphi(f_n)=1$ while $\int f_ng\to0$ by dominated convergence.
For a $\sigma$-finite measure, $(L^1)^* \cong L^\infty$.

:::

::: {.example title="$L^p$ is a Hilbert space only for $p=2$"}
If the measure space contains disjoint sets $E, F$ of measure $1$, then $f\coloneqq\chi_E$ and $g\coloneqq\chi_F$ satisfy $\norm{f+g}_p^2+\norm{f-g}_p^2 = 2\cdot 2^{2/p}$ and $2\norm f_p^2+2\norm g_p^2 = 4$, so the parallelogram law fails unless $p=2$.

:::

## Undergraduate analysis

::: {.example title="A pointwise limit of continuous functions need not be continuous"}
$f_n(x)\coloneqq x^n$ on $[0,1]$ converges pointwise to $\chi_{\theset{1}}$.

:::

::: {.example title="A uniform limit of differentiable functions need not be differentiable"}
$f_n(x)\coloneqq\sqrt{x^2+1/n}$ converges uniformly on $\RR$ to $\abs x$, which is not differentiable at $0$.
If $f_n$ are differentiable on $[a,b]$, $f_n'$ converges uniformly, and $f_n(x_0)$ converges for some $x_0\in[a,b]$, then $f_n$ converges uniformly to a differentiable $f$ with $f' = \lim f_n'$.

:::

::: {.example title="A differentiable function need not be continuously differentiable"}
$f(x)\coloneqq x^2\sin(1/x)$ for $x\neq0$ and $f(0)\coloneqq0$ is differentiable on $\RR$ with $f'(0)=0$, and $f'(x) = 2x\sin(1/x)-\cos(1/x)$ has no limit as $x\to0$.

:::

::: {.example title="A continuous function on a bounded set need not be uniformly continuous"}
$f(x)\coloneqq 1/x$ is continuous on $(0,1)$ and not uniformly continuous: $\abs{f(1/n)-f(1/(n+1))}=1$ while $\abs{1/n-1/(n+1)}\to0$.
A continuous function on a compact metric space is uniformly continuous.

:::

Further examples are on [[real-analysis/counterexamples-undergraduate|Undergraduate counterexamples]].
