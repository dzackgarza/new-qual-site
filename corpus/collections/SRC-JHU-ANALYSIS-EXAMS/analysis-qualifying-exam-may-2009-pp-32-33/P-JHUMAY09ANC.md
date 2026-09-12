---
schema: qual/card@1
id: P-JHUMAY09ANC
kind: problem
title: "Uniformly convergent holomorphic sequences with a single zero each"
classification:
  areas:
  - complex-analysis
  topics:
  - Hurwitz
  - Normal Families
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts and the uniform-convergence hypothesis with May 2009 problem 3 in the retained JHU extraction."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Repaired the unjustified varying-function continuity step by a compact-uniform estimate, proved the full zero-escape criterion, and supplied an example with a nonconstant zero-free limit and globally uniform convergence."
---

::: problem
Let $U\subset\mathbb C$ be connected and open, and let
$f_n:U\to\mathbb C$ be holomorphic with $f_n^{-1}(0)=\{c_n\}$
for every $n\geq1$. Suppose $f_n\to f_0$ uniformly on
$U$, where $f_0$ is nonconstant.

(a) Prove that $f_0$ has at most one zero in $U$.

(b) Can $f_0$ have no zeros? Give a necessary and
sufficient condition on $(c_n)$ for this to happen.
:::

::: solution
The zero-free case does occur. Its exact condition is
that $(c_n)$ eventually leaves every compact subset of $U$,
equivalently that it has no subsequence converging to a point
of $U$.

<1>1. The limit has at most one zero.
::: proof
Uniform convergence implies compact-uniform convergence,
so $f_0$ is holomorphic [@SS03]. Since it is nonconstant
on connected $U$, its zeros are isolated. If it had
distinct zeros $a,b$, choose disjoint closed disks around
them contained in $U$, with no zero of $f_0$ on either
boundary. The minimum of $|f_0|$ on the two boundaries
is positive. For sufficiently large $n$, uniform convergence
gives $|f_n-f_0|<|f_0|$ on both circles.

Rouché's theorem then gives at least one zero of $f_n$
in each disk, since $f_0$ has one in each [@SS03]. The
disjoint disks make these distinct, contradicting the
single-point fiber $f_n^{-1}(0)=\{c_n\}$. This proves (a).
:::

<1>2. A zero of the limit forces $c_n$ to converge to it.
::: proof
Suppose $f_0(a)=0$. For every sufficiently small $r>0$,
the closed disk $\overline{D(a,r)}$ lies in $U$ and
$f_0$ has no zero on its boundary. As in step <1>1,
Rouché's theorem shows that $f_n$ has a zero inside
this disk for all sufficiently large $n$. Its only
zero is $c_n$, so $|c_n-a|<r$ eventually. Such radii
can be chosen arbitrarily small; hence the entire
sequence $c_n$ converges to $a$.
:::

<1>3. An interior subsequential limit of the zeros is a zero of $f_0$.
::: proof
Suppose $c_{n_k}\to a\in U$. Choose a fixed compact
disk $K\subset U$ about $a$; it contains $c_{n_k}$
for all sufficiently large $k$. Since $f_{n_k}(c_{n_k})=0$,
$$
|f_0(a)|\leq |f_0(a)-f_0(c_{n_k})|
+\sup_{z\in K}|f_0(z)-f_{n_k}(z)|\longrightarrow0.
$$
The first term tends to zero by continuity of the fixed
function $f_0$, and the second by compact-uniform convergence.
Thus $f_0(a)=0$. Together with step <1>2, this proves
that $f_0$ is zero-free exactly when $(c_n)$ has no
subsequence converging inside $U$.

If the sequence does not eventually leave some compact
set $K\subset U$, infinitely many terms lie in $K$;
compactness yields an interior convergent subsequence.
Conversely, an interior convergent subsequence eventually
lies in a compact disk contained in $U$. This proves
the equivalent compact-escape formulation.
:::

<1>4. A nonconstant zero-free limit is possible under the stated uniform convergence.
::: proof
Take $U=D=\{|z|<1\}$ and
$$
c_n=1-\frac1{n+1},\qquad f_n(z)=z-c_n,
\qquad f_0(z)=z-1.
$$
Each $f_n$ has exactly the one zero $c_n\in D$, and
$\sup_{z\in D}|f_n(z)-f_0(z)|=1/(n+1)\to0$.
The limit $f_0$ is nonconstant and has no zero in $D$;
its only zero is the boundary point one. This supplies
the example required in (b) and verifies the criterion.
:::
:::
