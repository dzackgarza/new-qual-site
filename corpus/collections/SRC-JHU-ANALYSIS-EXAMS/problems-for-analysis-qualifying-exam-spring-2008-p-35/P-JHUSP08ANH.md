---
schema: qual/card@1
id: P-JHUSP08ANH
kind: problem
title: "Derivative bounds and extremal sequences for families of disk-valued holomorphic maps"
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with Spring 2008 problem 8 in the retained source. Its arbitrary-family wording does not permit rotation or control of other components; specified the full normalized family and retained counterexamples to the unqualified assertion."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked nonemptiness, the uniform derivative bound, derivative-phase normalization, the open-disk limit on the component of P, and locally uniform convergence on all other components."
---

::: problem
Let $U\subset\mathbb C$ be open and $P\in U$. Let
$\mathcal F$ be the family of **all** holomorphic maps
$f:U\to D=\{z:|z|<1\}$ such that $f(P)=0$.

(a) Prove that $S=\sup_{f\in\mathcal F}|f'(P)|$ is finite.

(b) Prove that there are $f_n\in\mathcal F$ converging
uniformly on compact subsets of $U$ to a holomorphic
$f_0:U\to D$ with $f_0'(P)=S$.
:::

::: remark
Part (b) fails for an arbitrary subfamily. For $U=D$,
$P=0$ and $\mathcal F=\{z\mapsto iz\}$, the supremum is
one but every sequence has derivative $i$, not one.
Disconnected domains cause another obstruction: on
$U=D(0,1)\cup D(3,1)$ take $P=0$ and, for $n\geq2$,
let $h_n(z)=(1-1/n)z$ on the first component and
$h_n=1-1/n$ on the second. The family $\{h_n:n\geq2\}$
has derivative supremum one. A sequence approaching that
supremum must have its indices tend to infinity, hence
converges to one on the second component, outside the
open target disk. The full family in the statement
allows both needed normalizations.
:::

::: solution
<1>1. The derivative supremum is a finite nonnegative real number.

::: proof
The zero function belongs to $\mathcal F$. Choose $r>0$
with $\overline{D(P,r)}\subset U$. Cauchy's derivative
formula and $|f|\leq1$ on that circle give
$$
|f'(P)|\leq\frac1r\qquad(f\in\mathcal F)
$$
[@SS03]. Thus $0\leq S\leq1/r<\infty$. This bound
also applies to every nonempty subfamily, proving (a).
:::

<1>2. A maximizing sequence can have real nonnegative derivatives and vanish off the component of $P$.

::: proof
Let $V$ be the connected component of $U$ containing $P$.
It is open, and $U\setminus V$ is open as a union of
the other components. For each $n\geq1$, choose
$g_n\in\mathcal F$ with $|g_n'(P)|>S-1/n$, using the
definition of supremum. Multiply $g_n$ on $V$ by
$\lambda_n=\overline{g_n'(P)}/|g_n'(P)|$ when its
derivative is nonzero, and use $\lambda_n=1$ otherwise.
Define $h_n=\lambda_ng_n$ on $V$ and $h_n=0$ on
$U\setminus V$. These are holomorphic maps into $D$
with $h_n(P)=0$, so belong to the full family, and
$$
h_n'(P)=|g_n'(P)|\longrightarrow S.
$$
This construction also covers $S=0$.
:::

<1>3. A subsequence has the required limit on all of $U$.

::: proof
The restrictions $h_n|_V$ are uniformly bounded by one.
Montel's theorem gives a subsequence $h_{n_j}$ converging
uniformly on compact subsets of $V$ to a holomorphic $h$
with $|h|\leq1$ and $h(P)=0$ [@SS03]. If $|h|=1$ at
any point of $V$, the maximum modulus principle would
make $h$ a constant of modulus one, contradicting $h(P)=0$.
Therefore $h(V)\subset D$.

Set $f_0=h$ on $V$ and $f_0=0$ on $U\setminus V$.
This is holomorphic and disk-valued. For any compact
$K\subset U$, the set $K\cap V$ is compact because $V$
is closed relative to $U$. On that set the subsequence
converges uniformly, and on $K\setminus V$ it is identically
zero. Thus convergence to $f_0$ is uniform on every such $K$.
Finally, on a fixed small circle centered at $P$ inside $V$,
Cauchy's derivative formula gives
$$
|h_{n_j}'(P)-f_0'(P)|
\leq\frac1r\sup_{|z-P|=r}|h_{n_j}(z)-f_0(z)|\longrightarrow0.
$$
Step <1>2 now yields $f_0'(P)=S$. Relabeling this
subsequence as $(f_j)$ proves (b), including attainment
of the specified real derivative rather than only its modulus.
:::
:::
