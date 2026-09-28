---
schema: qual/card@1
id: P-BERK89S-13
kind: problem
title: Center of the dihedral group $D_n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the rotation-reflection normal form in $D_n$: a rotation $r^k$ is
    central exactly when $2k$ is divisible by $n$, and no reflection commutes
    with the basic rotation for $n\ge3$.
---

::: {.problem}
Let $D_n$ be the group of rigid motions of a regular $n$-gon, $n\ge3$. Determine its center
\[
Z(D_n)=\{c\in D_n:cx=xc\text{ for every }x\in D_n\}.
\]
:::

::: {.solution}
Let $r$ be the rotation through angle $2\pi/n$ and let $s$ be a reflection.
Then every element of $D_n$ has a unique form $r^k$ or $r^ks$, with
$0\leq k<n$, and
$$
r^n=s^2=e,
\qquad
srs=r^{-1}.
$$

<1>1. A rotation $r^k$ is central if and only if $n$ divides $2k$.

::: {.proof}
Every rotation commutes with $r$, so $r^k$ is central exactly when it also
commutes with $s$. From $srs=r^{-1}$ one obtains
$$
sr^k=r^{-k}s.
$$
Hence
$$
r^ks=sr^k
\quad\Longleftrightarrow\quad
r^ks=r^{-k}s
\quad\Longleftrightarrow\quad
r^{2k}=e.
$$
Since $r$ has order $n$, the last condition is equivalent to $n\mid2k$.
:::

<1>2. No reflection $r^ks$ lies in the center of $D_n$.

::: {.proof}
For any $k$,
$$
(r^ks)r=r^k(sr)=r^{k-1}s,
$$
whereas
$$
r(r^ks)=r^{k+1}s.
$$
If these were equal, then $r^{k-1}=r^{k+1}$, so $r^2=e$. This would force
$n\mid2$, impossible because $n\geq3$. Thus no reflection commutes with $r$.
:::

<1>3. The center is
$$
\boxed{
Z(D_n)=
\begin{cases}
\{e\},&n\text{ odd},\\
\{e,r^{n/2}\},&n\text{ even}.
\end{cases}
}
$$

::: {.proof}
By step <1>2, every central element is a rotation. Step <1>1 says that the
central rotations are exactly the $r^k$ with $2k\equiv0\pmod n$.

If $n$ is odd, multiplication by $2$ is invertible modulo $n$, so only
$k\equiv0\pmod n$ occurs. If $n$ is even, the solutions modulo $n$ are
$k\equiv0$ and $k\equiv n/2$. These give the two stated cases.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested center.
:::
:::
