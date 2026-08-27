---
order: 35
---

# Sequences and Series

## Sequences

## Sequences of functions

[[D-S2YWR]]

:::{.example}
A series of continuous functions that does *not* converge uniformly but is still continuous:
\[  
g(x) \da \sum {1 \over 1 + n^2 x}
.\]

Take $x = 1/n^2$.

:::

## Sequences of number

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

[[PR-P6NHI]]

[[PR-UJ64S]]
[[C-3S4XS]]
[[PR-GT5RS]]

[[PR-H4CYN]]

[[PR-6OHTJ]]

[[PR-LEDI3]]

[[C-VSE32]]

[[PR-4RWAG]]

[[T-EWZ5U]]

## Uniform Convergence

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
