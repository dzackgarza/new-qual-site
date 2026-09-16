---
schema: qual/card@1
id: P-JHUFA11ANC
kind: problem
title: Finite valence excludes an essential singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked September 2011 problem 3 and the preceding unit-disk convention on PDF page 22; restored the definition of D and replaced the truncated title."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved density at an essential singularity by the bounded reciprocal argument, then constructed n+1 disjoint preimage neighborhoods with a common image value; no multiplicity assumption or Great Picard theorem is used."
---

::: {.problem}
Let $D=\{z\in\mathbb C:|z|<1\}$ and let $f$ be
holomorphic on $D\setminus\{0\}$. Suppose there is a
positive integer $n$ such that $f^{-1}(w)$ contains at
most $n$ points for every $w\in\mathbb C$. Prove that
zero is a removable singularity or a pole.
:::

::: {.solution}
Suppose, for a contradiction, that zero is an essential
singularity. In particular $f$ is nonconstant.

<1>1. The image of every punctured disk about zero is dense in $\mathbb C$.

::: {.proof}
Fix $0<r<1$. If $f(\{0<|z|<r\})$ were not dense,
there would be $w\in\mathbb C$ and $\delta>0$ such that
$|f(z)-w|\geq\delta$ throughout this punctured disk.
Then $g(z)=1/(f(z)-w)$ is holomorphic and bounded by
$1/\delta$ there. It extends holomorphically across zero
by the removable-singularity theorem [@SS03]; denote
the extension by $G$.

If $G(0)\ne0$, the identity $f=w+1/G$ extends $f$
holomorphically across zero. If $G(0)=0$, then $G$ is
not identically zero, since it is nonzero on the punctured
disk. Its Taylor expansion has the form $G(z)=z^mH(z)$
with $m\geq1$ and $H(0)\ne0$. Consequently
$f(z)=w+z^{-m}/H(z)$ has a pole at zero. Both alternatives
contradict essentiality. Thus the image must be dense.
:::

<1>2. There are $n+1$ pairwise disjoint disks whose images have nonempty intersection.

::: {.proof}
Choose an open disk $B_1$ with closure contained in
$D\setminus\{0\}$. The restriction of $f$ to $B_1$ is
nonconstant: otherwise the identity theorem on the
connected punctured disk would make $f$ constant everywhere.
Thus $V_1=f(B_1)$ is nonempty and open by the open mapping
theorem [@SS03].

Inductively, suppose $B_1,\ldots,B_k$ have pairwise
disjoint closures in $D\setminus\{0\}$ and
$V_k=\bigcap_{j=1}^k f(B_j)$ is nonempty and open.
Choose $r>0$ so small that $r<1$ and the punctured disk
$0<|z|<r$ misses all those closures. Step <1>1 gives
a point $a$ in this punctured disk with $f(a)\in V_k$.
Choose an open disk $B_{k+1}$ about $a$ whose closure
is contained in $0<|z|<r$. It is disjoint from all
the earlier closures. Its image is open by the same
nonconstancy and open mapping argument. Hence
$$
V_{k+1}=V_k\cap f(B_{k+1})
$$
is open and contains $f(a)$, so it is nonempty.
This completes the induction up to $k=n+1$.
:::

<1>3. The common image value contradicts the fiber bound.

::: {.proof}
Choose $w\in\bigcap_{j=1}^{n+1}f(B_j)$. For each $j$
there is $z_j\in B_j$ with $f(z_j)=w$. The disks are
disjoint, so these are $n+1$ distinct points of $f^{-1}(w)$,
contrary to the hypothesis. Zero is therefore not essential.
The classification of isolated singularities leaves only
a removable singularity or a pole [@SS03], as required.
:::
:::
