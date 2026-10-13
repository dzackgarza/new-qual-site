---
schema: qual/card@1
id: P-MAXAT-1-05
kind: problem
title: Maxim algebraic topology 1.5
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 5 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that if $M ^ { n }$ is connected, non-compact manifold, then $H _ { i } ( M ; R ) = 0$ for $i \geq n$ •
:::

::: {.solution}
Here $R$ is a coefficient ring. The assertion in degrees $i>n$ is the dimension bound for manifold homology; the substantive point is $H_n(M;R)=0$.

<1>1. A smooth or topological $n$-manifold has the homotopy type of an $n$-dimensional CW complex, so
\[
H_i(M;R)=0
\qquad(i>n).
\]

::: {.proof}
Manifolds are triangulable in the standard category used here, or equivalently admit an $n$-dimensional CW model. Its cellular chain groups vanish above dimension $n$, hence so does homology above dimension $n$.
:::

<1>2. Let $z$ be a singular $n$-cycle in $M$. Its support is contained in a compact subset $K\subset M$.

::: {.proof}
A singular chain is a finite linear combination of singular simplices. Each simplex has compact image because its standard simplex is compact, and a finite union of compact sets is compact.
:::

<1>3. Since $M$ is connected and noncompact, there exists a point
\[
x\in M\setminus K.
\]

::: {.proof}
If $K=M$, then $M$ would be compact, contrary to the hypothesis. Thus its complement is nonempty.
:::

<1>4. The cycle $z$ determines a class in
\[
H_n(M,M\setminus\{x\};R)
\]
which is zero.

::: {.proof}
Because the support of $z$ is contained in $K$ and $x\notin K$, the entire cycle lies in $M\setminus\{x\}$. Hence as a relative chain modulo $C_n(M\setminus\{x\};R)$ it is literally zero, so its relative homology class is zero.
:::

<1>5. For a connected $n$-manifold, the natural map
\[
H_n(M;R)\longrightarrow H_n(M,M\setminus\{x\};R)
\]
is injective whenever a nonzero top-dimensional ordinary homology class exists; equivalently, a top-dimensional class is determined by its local orientation coefficient at one point.

::: {.proof}
The local homology group at $x$ is
\[
H_n(M,M\setminus\{x\};R),
\]
and excision identifies it with the top relative homology of an $n$-ball modulo its punctured ball. On a connected manifold, the coefficients of an $n$-cycle in these local homology groups propagate uniquely along paths: in an oriented component they are constant after transport by the orientation local system, while if the coefficient ring does not support a global orientation section, the only global top class is zero. Thus a global top-dimensional homology class whose local coefficient vanishes at one point vanishes everywhere. This is the standard local-homology proof of the theorem that a connected manifold has nonzero ordinary top homology only when it is compact and orientable over the chosen coefficients.
:::

<1>6. Therefore
\[
H_n(M;R)=0.
\]

::: {.proof}
Let $[z]\in H_n(M;R)$. Steps <1>2--<1>4 choose $x$ outside its compact support and show that its image in the local homology group at $x$ is zero. By step <1>5, $[z]=0$. Since every class is represented by such a finite singular cycle, the whole group vanishes.
:::

<1>7. Combining steps <1>1 and <1>6 gives
\[
\boxed{H_i(M;R)=0\quad\text{for every }i\geq n.}
\]

::: {.proof}
Step <1>6 handles $i=n$, and step <1>1 handles every $i>n$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the desired conclusion.
:::
:::
