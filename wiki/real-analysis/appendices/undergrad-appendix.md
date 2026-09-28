---
title: Undergraduate review
order: 43
---

# Undergraduate review

## Limits superior

[[D-G2I5Q]]

::: {.example title="The supremum and the limit superior differ"}
For $x_n \coloneqq \frac{n+1}{n}$, $\sup_n x_n = x_1 = 2$, while $x_n\to1$, so $\limsup_n x_n = 1$.

:::

## Convergence theorems

[[T-TRW6N]]

::: {.theorem title="Fatou's lemma"}
If $f_n \geq 0$ are Lebesgue measurable functions on $\RR^d$ and $f_n\to f$ pointwise, then
$$
\int f \leq \liminf_{n\to\infty} \int f_n.
$$

:::

::: {.proof}
Let $g$ be a bounded measurable function supported on a set of finite measure with $0\leq g\leq f$, and let $g_n \coloneqq \min(g, f_n)$.
Then $g_n\to\min(g,f) = g$ pointwise, and the $g_n$ are uniformly bounded and supported in the support of $g$, so the bounded convergence theorem gives $\int g_n\to\int g$.
Since $\int g_n\leq\int f_n$, this gives $\int g\leq\liminf_n\int f_n$.
Taking the supremum over all such $g$ gives $\int f\leq\liminf_n\int f_n$.

:::

::: {.theorem title="Monotone convergence theorem"}
If $0 \leq f_1 \leq f_2 \leq \cdots$ are Lebesgue measurable functions and $f(x) \coloneqq \lim_n f_n(x)$, then
$$
\int f = \lim_{n\to\infty} \int f_n.
$$

:::

::: {.proof}
Since $f_n\leq f$, $\limsup_n\int f_n\leq\int f$, and Fatou's lemma gives $\int f\leq\liminf_n\int f_n$.

:::

## Differentiation

::: {.fact}
Let $f\colon[a,b]\to\RR$.

- If $f$ is monotone, or more generally of bounded variation, then $f'(x)$ exists for almost every $x$ and $\int_a^b\abs{f'} < \infty$.

- The Cantor function has bounded variation and $f'=0$ almost everywhere, but it is not constant, so $f(x) - f(a) = \int_a^x f'$ can fail for $f$ of bounded variation.

- If $f$ is absolutely continuous, then $f(x) = f(a) + \int_a^x f'$ for all $x\in[a,b]$.

- If $f\in L^1([a,b])$, then $F(x) \coloneqq\int_a^x f$ is absolutely continuous and $F' = f$ almost everywhere.

:::

::: {.corollary title="Lebesgue density theorem"}
If $E\subseteq\RR$ is a Lebesgue measurable set of finite measure and $m$ is Lebesgue measure, then for almost every $x\in E$,
$$
\lim_{r\to 0}\frac{m(E\cap B(x,r))}{m(B(x,r))} = 1.
$$

:::

::: {.proof}
Apply the last item of the preceding fact to $f\coloneqq\chi_E$.

:::

::: {.theorem title="A continuous nowhere differentiable function"}
There exists a continuous function $f\colon\RR\to\RR$ that is differentiable at no point.

:::

::: {.remark}
Weierstrass's function $\sum_{n\geq0} a^n\cos(b^n\pi x)$ with $0<a<1$, $b$ an odd positive integer, and $ab>1+3\pi/2$ is such a function; see [[real-analysis/counterexamples-undergraduate#The Weierstrass function|Undergraduate counterexamples]].
The construction takes $f(x)\coloneqq\sum_{n\geq1} a_n\sin(b_nx)$ with $\sum a_n<\infty$ and $a_nb_n\to\infty$ rapidly, for example $a_n = 10^{-n}$ and $b_n = 10^{6n}$.
For each $n$ and $x$, an increment $\Delta x$ of size comparable to $1/b_n$ makes the $n$th term change by an amount comparable to $a_n$, while the terms with $k<n$ change by at most $\sum_{k<n}a_kb_k/b_n$, which is small compared with $a_n$, and the terms with $k>n$ change by at most $\sum_{k>n}2a_k$, also small compared with $a_n$.
So $\abs{\Delta f/\Delta x}$ is comparable to $a_nb_n\to\infty$, and $f'(x)$ does not exist.

:::

## Baire category

[[D-2MJRE]]

[[D-5NODS]]

::: {.definition}
A subset of a topological space is \dfn{residual} if its complement is [[D-5NODS|meager]].

:::

::: {.example}
Every countable subset of $\RR$, such as $\QQ$, is meager, since each point is closed with empty interior.

:::

::: {.fact}
In a topological space $X$:

- a subset of a meager set is meager;

- a countable union of meager sets is meager;

- a countable intersection of residual sets is residual;

- a countable intersection of dense open sets is residual.

If $X$ is a complete metric space, the Baire category theorem states that every residual subset of $X$ is dense, and in particular nonempty.

:::

[[P-HCA6D]]
