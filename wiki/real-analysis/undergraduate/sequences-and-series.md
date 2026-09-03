---
order: 35
problems:
  topics:
  - Sequences of Numbers
  - Series of Numbers
  - Series of Functions
  - Limits
---

# Sequences and Series

## Sequences of functions

Pointwise convergence allows the index \(N\) to depend on \(x\); uniform convergence
does not.  That quantifier change is what later permits continuity to pass through the
limit; on finite-measure domains, uniform convergence also controls passage of the
integral through the limit.  The limsup of functions is useful when an actual pointwise
limit is unavailable, while the example below is a reminder that continuity of the
limit does not by itself imply uniform convergence of the approximating series.

[[D-S2YWR]]

:::{.example}
On $(0,1]$, consider
\[
g(x) \da \sum_{n=1}^{\infty} {1 \over 1 + n^2 x}.
\]
For every $a>0$ the series converges uniformly on $[a,1]$ by comparison with
$\sum_{n\ge1}(n^2a)^{-1}$, so $g$ is continuous on $(0,1]$.
The convergence is not uniform on $(0,1]$: for the $n$th summand,
\[
{1\over 1+n^2(1/n^2)}={1\over2},
\]
so the summands do not even converge uniformly to zero.

:::

## Sequences of numbers

:::{.slogan}
$\limsup$ is largest limit of a convergent subsequence, $\liminf$ is the smallest.

:::

[[PR-4EVYE]]

[[FF-QLRXX]]

[[FD-D2QPH]]

:::{.proof title="showing a useful trick"}
Show that
\[
\sum a_k \leq \sum 2^k a_{2^k} \leq 2 \sum a_k
\]
using 
\[
\sum a_k = a_0 + a_1 + a_2 + a_3 + \cdots
\leq \qty{a_1} + \qty{a_2 + a_2} + \qty {a_3 + a_3 + a_3 + a_3} + \cdots \\
\]
where each group with $a_k$ has $2^k$ terms.

:::

## Series

For numerical series, the Cauchy criterion is the underlying test: every sufficiently
late tail must be small.  Comparison and \(p\)-tests turn that criterion into practical
sufficient tests.  For a function's Taylor series, Taylor's theorem and its remainder
determine when the formal expansion actually converges back to the function.  For series
of functions, the same tail criterion is applied in a function norm when uniform control
is needed.

[[PR-P6NHI]]

[[PR-UJ64S]]
[[C-3S4XS]]
[[PR-GT5RS]]

[[PR-H4CYN]]

[[PR-6OHTJ]]

[[PR-LEDI3]]

[[C-VSE32]]

[[PR-4RWAG]]

[[T-2R7PC]]

## Uniform Convergence

The sup norm packages uniform convergence as

\[
f_n\to f \text{ uniformly}
\quad\Longleftrightarrow\quad
\|f_n-f\|_\infty\to 0.
\]

To prove it, bound the supremum independently of \(x\); to disprove it, choose points
\(x_n\) where the error stays bounded below.  For a series, the Weierstrass \(M\)-test
reduces the same problem to convergence of a numerical majorant.

[[PR-WUZSG]]

[[FF-I6VGK]]

[[FS-FZL2X]] [[FS-THMMW]]

[[FF-IAUQG]] [[FS-5FKPD]]

:::{.remark title="Negating the Sup Norm test"}
**Negating**: find an $x$ which depends on $n$ for which $\norm{f_n}_\infty > \eps$ (negating small tails) or $\norm{f_n - f_m} > \eps$ (negating the Cauchy criterion).

:::

[[PR-RWROV]]

:::{.proof}
\envlist

1.  Let $\theset{f_k}$ be Cauchy in $X$.

2.  Define a candidate limit using pointwise convergence:

    Fix an $x$; since
  \[
  \abs{f_k(x) - f_j(x)}  \leq \norm{f_k - f_k} \to 0
  \] 
    the sequence $\theset{f_k(x)}$ is Cauchy in $\RR$.
    So define $f(x) \definedas \lim_k f_k(x)$.

3.  Show that $\norm{f_k - f} \to 0$:
  \[
  \abs{f_k(x) - f_j(x)} < \varepsilon ~\forall x \implies \lim_{j} \abs{f_k(x) - f_j(x)} <\varepsilon ~\forall x
  \]
    Alternatively, $\norm{f_k-f} \leq \norm{f_k - f_N} + \norm{f_N - f_j}$, where $N, j$ can be chosen large enough to bound each term by $\varepsilon/2$.

4.  Show that $f\in X$:

    The uniform limit of continuous functions is continuous.

:::

:::{.remark}
In other cases, you may need to show the limit is bounded, or has bounded derivative, or whatever other conditions define $X$.

:::

[[T-3QNBQ]]

[[FT-ITKJU]]
