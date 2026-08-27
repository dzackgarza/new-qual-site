---
order: 0
---

# Integration

:::{.remark title="A common proof technique"}
\envlist

- Show something holds for indicator functions.
- Show it holds for simple functions by linearity.
- Use $s_k \increasesto f$ and apply MCT to show it holds for $f$.

:::

:::{.remark title="on notation"}
\envlist

- $L^+$: nonnegative measurable functions
- $L^1$: Lebesgue integrable functions, so $\int \abs{f} < \infty$

:::

:::{.remark title="on notation"}
\envlist

- $L^+$: nonnegative measurable functions
- $L^1$: Lebesgue integrable functions, so $\norm{f}_{L^1} \da \int \abs{f} < \infty$.

:::

[[D-DHFN4]]

[[FD-OFT7I]] [[FD-OOCQD]]

:::{.remark}
Note that we still require Borel sets in the target for Lebesgue measurability!
Taking $(\mcl_{\RR^d}, \mcl_\RR)$ functions is too stringent, e.g. this class does not contain continuous functionals.

:::

:::{.warnings}
If $f$ is $\mcl\dash$measurable and $h$ is continuous, it's not necessarily true that $k\da f\circ h$ is $\mcl\dash$measurable.
Standard counterexample: set $g(x) \da C(x) + x$ for $C$ the Cantor-Lebesgue function, then $g:[0, 1]\to [0, 2]$ is a homeomorphism.
Then $m(g(C)) = 1$ since $f$ is constant on intervals in $C^c$, so use Vitali's theorem: a set is null iff every subset is measurable.
So $g(C)$ contains a non-measurable set $A$.
Define $B\da g\inv(A)$, then $B \subset C$ and $m(C) = 0$ implies $B$ is measurable and $\chi_B$ is a measurable function.
But then $k\da \chi_B \circ g\inv$ is not $\mcl\dash$measurable, since $k\inv(1) = A$ is a non-measurable set, but $\chi_B$ is $\mcl\dash$measurable and $g\inv$ is continuous.

:::

[[PR-EWXRO]]

[[D-553MO]]

[[PR-KTKT6]]

[[D-R4VKE]]

[[FD-Q3XHG]]

:::{.remark title="Integrals split across disjoint sets"}
A useful fact: for $(X, \mathcal{M})$ a measure space, integrals split across disjoint sets:
\[
\int_X f = \int_{X\sm A} f + \int_A f && \forall\, A \in \mathcal{M} 
.\]

:::

[[D-YWRVG]]

:::{.example title="An essentially bounded but not bounded function"}
$f(x) = x\chi_\QQ(x)$ is essentially bounded but not bounded.

:::

[[PR-OI5HX]]

[[T-YSMII]]

[[FF-EMDBP]]

[[FF-C7GY4]] [[FF-LMANJ]]

:::{.slogan}
Large powers of $x$ help us in neighborhoods of infinity and hurt around zero.

:::

## The Convergence Theorems

[[T-5K3IO]]

[[FT-5G4Y3]]

:::{.slogan}
Measurable, non-negative, increasing pointwise a.e. allows commuting limits and integrals.

:::

:::{.proof title="of MCT"}
Write $f\da \lim_n f_n\in[0,\infty]$, which exists almost everywhere by monotonicity, and set $f=0$ on the null set where the limit fails.
The integrals $\int f_n$ are increasing in $[0,\infty]$, so $\alpha\da \lim_n \int f_n$ exists in $[0,\infty]$, and $f_n\leq f$ gives $\alpha\leq \int f$.

For the reverse inequality, let $0\leq \varphi\leq f$ be simple and fix $0<c<1$.
The sets $E_n\da \theset{x\st f_n(x)\geq c\varphi(x)}$ increase to the set where $f\geq c\varphi$, which is almost all of $X$ because $f_n\nearrow f$ and $c\varphi < \varphi\leq f$ wherever $\varphi>0$.
Then
\[
\int f_n
\geq \int_{E_n} f_n
\geq c\int_{E_n}\varphi
,\]
and continuity of measure from below (each simple $\varphi$ is a finite linear combination of indicators of finite-measure sets, or the identity $\int_{E_n}\varphi\to\int\varphi$ in $[0,\infty]$) yields $\alpha\geq c\int\varphi$.
Let $c\nearrow 1$, then take the supremum over simple $\varphi\leq f$, to conclude $\alpha\geq \int f$.

:::

[[T-IJQQG]]

[[FT-LCR5P]]

:::{.proof title="of DCT"}
The pointwise limit $f$ is measurable, and $\abs{f}\leq g$ almost everywhere, so $f\in L^1$.
The functions $2g-\abs{f_n-f}$ are nonnegative and converge pointwise almost everywhere to $2g$, so Fatou's lemma (below) gives
\[
\int 2g
= \int \liminf_n \bigl(2g-\abs{f_n-f}\bigr)
\leq \liminf_n \int \bigl(2g-\abs{f_n-f}\bigr)
= \int 2g - \limsup_n \int \abs{f_n-f}
.\]
Thus $\limsup_n \int \abs{f_n-f}\leq 0$, so $\int\abs{f_n-f}\to 0$.
Then $\abs{\int f_n - \int f} \leq \int\abs{f_n-f}\to 0$.

:::

[[T-WYX24]]

:::{.proof title="of generalized DCT"}
Proceed by showing $\limsup \int f_n \leq \int f \leq \liminf \int f_n$:

- $\int f \geq \limsup \int f_n$:
\[
\int g - \int f 
&= \int \qty{g-f} \\
&\leq \liminf \int \qty{g_n - f_n} \quad \text{Fatou} \\
&= \lim \int g_n + \liminf \int (-f_n) \\
&= \lim \int g_n - \limsup \int f_n \\
&= \int g - \limsup \int f_n \\
\\
\implies \int f &\geq \limsup \int f_n
.\]

  - Here we use $g_n - f_n \converges{n\to\infty}\too g-f$ with $0 \leq \abs{f_n} - f_n \leq g_n - f_n$, so $g_n - f_n$ are nonnegative (and measurable) and Fatou's lemma applies.

- $\int f \leq \liminf \int f_n$:
\[
\int g + \int f 
&= \int(g+f) \\
&\leq \liminf \int \qty{g_n + f_n} \\
&= \lim \int g_n + \liminf \int f_n \\
&= \int g + \liminf f_n \\
\\
\int f &\leq \liminf \int f_n
.\]

  - Here we use that $g_n + f_n \to g+f$ with $0 \leq \abs{f_n} + f_n \leq g_n + f_n$ so Fatou's lemma again applies.

:::

[[PR-KNYSF]]

:::{.remark}
The converse to the DCT does not hold, i.e. $L^p$ boundedness does not imply a.e. boundedness, i.e. it is not true that $\lim \int f_k = \int f$ implies that $\exists g\in L^p$ such that $f_k < g$ a.e. for every $k$.

Take

- $b_k = \sum_{j=1}^k \frac 1 j \to \infty$

- $f_k = \chi_{[b_k, b_{k+1}]}$

Then

- $f_k \converges{a.e.}\to f = 0$,

- $\int f_k = \frac 1 k \to 0 \implies \norm{f_k}_p \to 0$,

- $0 = \int f = \lim \int f_k = 0$

- But $g > f_k \implies g > \norm{f_k}_\infty = 1$ a.e. $\implies g\not\in L^p(\RR)$.

:::

[[PR-H4ZVI]]

:::{.proof title="That $L^1$ convergence implies convergence of norms"}
Let $g_n = \abs{f_n} - \abs{f_n - f}$, then $g_n \to \abs{f}$ and 
\[
\abs{g_n} = \abs{ \abs{f_n} - \abs{f_n - f} } \geq \abs{f_n - (f_n - f)} = \abs{f} \in L^1
,\]
so the DCT applies to $g_n$ and
\[
\norm{f_n - f}_1 = \int \abs{f_n - f} + \abs{f_n} - \abs{f_n}
= \int \abs{f_n} - g_n\\
\to_{DCT} \lim \int \abs{f_n} - \int \abs{f}
.\]

:::

[[T-LDJNS]]

[[FT-P5UNP]]

:::{.proof title="of Fatou"}
Let $g_n\da \inf_{k\geq n} f_k$.
Then $0\leq g_n\nearrow \liminf_k f_k$, so the monotone convergence theorem gives
\[
\int \liminf_n f_n
= \lim_n \int g_n
\leq \liminf_n \int f_n
,\]
because $g_n\leq f_n$ for each $n$.

The companion inequality $\limsup_n \int f_n \leq \int \limsup_n f_n$ is false in general: $f_n = n\chi_{[0,1/n]}$ has $\int f_n=1$ and $\limsup_n f_n=0$ almost everywhere.
It does hold if $0\leq f_n\leq g$ with $g\in L^1$, by applying the liminf form to $g-f_n$.

:::
[[T-6PRW3]]

[[FT-4JRQX]]
[[T-4GPEF]]

[[FT-T7OAO]]
[[T-X7XZX]]

[[FT-H6AWV]] [[FT-VHK2H]]
[[PR-V4MOK]]
[[PR-JW3QE]]

:::{.proof title="Commuting sums with integrals"}
- Idea: MCT.
- Let $F_N = \sum^N f_n$ be a finite partial sum;
- Then there are simple functions $\phi_n \nearrow f_n$
- So $\sum^N \phi_n \nearrow F_N$ and MCT applies

:::
[[T-MN6WQ]]

[[FS-BM2PV]]

:::{.proof title="Commuting sums with integrals (integrable)"}
\envlist

- By Tonelli, if $f_n(x) \geq 0$ for all $n$, taking the counting measure allows interchanging the order of "integration".
- By Fubini on $\abs{f_n}$, if either "iterated integral" is finite then the result follows.

:::
[[PR-EHIXY]]

[[FR-KEWV2]]

:::{.proof title="Absolute $L^1$ summability"}
Nonnegativity of $\abs{f_k}$ and the monotone convergence theorem give
\[
\int \sum_k \abs{f_k}
= \sum_k \int \abs{f_k}
= \sum_k \norm{f_k}_1
< \infty
,\]
so $\sum_k \abs{f_k(x)}<\infty$ for almost every $x$, and $\sum_k f_k(x)$ converges absolutely almost everywhere.
The partial sums $F_N\da\sum_{k=1}^N f_k$ are Cauchy in $L^1$:
\[
\norm{F_{N+M}-F_N}_1
\leq \sum_{k=N+1}^{N+M} \norm{f_k}_1
,\]
which is a tail of a convergent series.
Completeness of $L^1$ supplies $F\in L^1$ with $F_N\to F$ in $L^1$.
A subsequence then converges to $F$ almost everywhere, hence $F=\sum_k f_k$ almost everywhere.

:::

:::{.example title="Using Fatou to compute the limit of a sequence of integrals"}
\[
\lim _{n \rightarrow \infty} \int_{0}^{\infty} \frac{n^{2}}{1+n^{2} x^{2}} e^{-\frac{x^{2}}{n^{3}}} d x
\overset{\text{Fatou}}\geq
\int_{0}^{\infty} \lim _{n \rightarrow \infty}  \frac{n^{2}}{1+n^{2} x^{2}} e^{-\frac{x^{2}}{n^{3}}} d x \to \int \infty
.\]

Note that MCT might work, but showing that this is non-decreasing in $n$ is difficult.

:::

## Commuting 

[[PR-NKZBT]]

:::{.proof title="Commuting sums with integrals, non-negative case"}
- Idea: MCT. 
- Let $F_N = \sum^N f_n$ be a finite partial sum; 
- Then there are simple functions $\phi_n \nearrow f_n$ 
- So $\sum^N \phi_n \nearrow F_N$ and MCT applies

:::

:::{.proof title="Commuting sums with integrals, integrable case"}
\envlist

- By Tonelli, if $f_n(x) \geq 0$ for all $n$, taking the counting measure allows interchanging the order of "integration".
- By Fubini on $\abs{f_n}$, if either "iterated integral" is finite then the result follows.

:::

[[PR-YJJSY]]

:::{.proof}
Define $F_N = \sum^N f_k$ and $F = \lim_N F_N$, then $\norm{F_N}_1 \leq \sum^N \norm{f_k} < \infty$ so $F\in L^1$ and $\norm{F_N - F}_1 \to 0$ so the sum converges in $L^1$.
Almost everywhere: $\sum \abs{f_k}$ has finite integral by monotone convergence, hence is finite almost everywhere, so $\sum f_k$ converges absolutely almost everywhere, and the $L^1$ limit agrees with that pointwise sum.

:::

[[PR-2CZUM]]
