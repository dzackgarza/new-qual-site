---
schema: qual/card@1
id: P-MAXAT-6-08
kind: problem
title: Maxim algebraic topology 6.8
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 8 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find the smallest k such that $\mathbb { C P } ^ { n }$ can be smoothly embedded in $\mathbb { R } ^ { 2 n + k }$
:::

As stated for arbitrary $n$, this is not a problem with a known closed-form
answer. The exact Euclidean embedding dimension of $\mathbb{CP}^n$ is a
classical embedding problem. The standard results give sharp answers for many
families and nontrivial intervals in the remaining cases.

For a positive integer $n$, write
\[
\alpha(n)
\]
for the number of $1$'s in the binary expansion of $n$, and define
\[
N(n)
\coloneqq
\min\left\{
N:
\mathbb{CP}^n
\text{ admits a smooth embedding into }\mathbb R^N
\right\}.
\]
Then the requested number is
\[
k_{\min}(n)=N(n)-2n.
\]

::: pf

::: pf-step

A classical nonembedding theorem gives
\[
N(n)
>
4n-2\alpha(n).
\]
Equivalently,
\[
N(n)
\ge
4n-2\alpha(n)+1.
\]


::: pf-proof

This is the Atiyah--Hirzebruch/Feder--Segal nonembedding theorem for complex
projective spaces. In the notation used here, it states that
\[
\mathbb{CP}^n
\not\hookrightarrow
\mathbb R^{,4n-2\alpha(n)}.
\]
See the embedding results surveyed in the standard projective-space
immersion literature, for example Feder--Segal,
*Immersions and embeddings of projective spaces*.

Since $N(n)$ is an integer, the strict inequality is equivalent to the
displayed integer lower bound.

:::

:::

::: pf-step

Mukherjee's embedding theorem gives
\[
N(n)
\le
4n-\alpha(n).
\]
If $n>1$ is odd, it improves to
\[
N(n)
\le
4n-\alpha(n)-1.
\]


::: pf-proof

These are the embeddings constructed by A. Mukherjee,
*Embedding complex projective spaces in Euclidean space*,
Bull. London Math. Soc. 13 (1981), 323--324.

:::

:::

::: pf-step

Hence for arbitrary $n$ one has
\[
\boxed{
2n-2\alpha(n)+1
\le
k_{\min}(n)
\le
2n-\alpha(n).
}
\]
For odd $n>1$,
\[
\boxed{
2n-2\alpha(n)+1
\le
k_{\min}(n)
\le
2n-\alpha(n)-1.
}
\]


::: pf-proof

Subtract the real dimension
\[
2n
\]
of $\mathbb{CP}^n$ from the lower bound in step <1>1 and the upper bounds in
step <1>2.

:::

:::

::: pf-step

If
\[
\alpha(n)=1,
\]
equivalently
\[
n=2^r,
\]
then the bounds coincide and
\[
\boxed{
N(n)=4n-1,
\qquad
k_{\min}(n)=2n-1.
}
\]


::: pf-proof

When $\alpha(n)=1$, step <1>1 gives
\[
N(n)
\ge
4n-1.
\]
Step <1>2 gives
\[
N(n)
\le
4n-1.
\]
Thus equality holds.

For $n=1$, this is the familiar embedding
\[
\mathbb{CP}^1\cong S^2\hookrightarrow\mathbb R^3.
\]

:::

:::

::: pf-step

If $n>1$ is odd and
\[
\alpha(n)=2,
\]
then
\[
\boxed{
N(n)=4n-3,
\qquad
k_{\min}(n)=2n-3.
}
\]


::: pf-proof

Step <1>1 gives
\[
N(n)
>
4n-4,
\]
so
\[
N(n)\ge4n-3.
\]
Because $n$ is odd, the improved upper bound in step <1>2 gives
\[
N(n)
\le
4n-\alpha(n)-1
=
4n-3.
\]
Hence equality holds.

:::

:::

::: pf-step

If $n$ is even and
\[
\alpha(n)=2,
\]
then
\[
\boxed{
N(n)=4n-2,
\qquad
k_{\min}(n)=2n-2.
}
\]


::: pf-proof

Sanderson--Schwarzenberger's nonimmersion theorem implies in this case that
\[
\mathbb{CP}^n
\not\looparrowright
\mathbb R^{,4n-3}.
\]
In particular it cannot embed there, so
\[
N(n)\ge4n-2.
\]

Mukherjee's upper bound from step <1>2 gives
\[
N(n)
\le
4n-\alpha(n)
=
4n-2.
\]
Thus equality holds.

:::

:::

::: pf-step

The bounds do not coincide for all $n$; for example
\[
n=7
\]
gives only
\[
\boxed{
N(7)\in\{23,24\},
\qquad
k_{\min}(7)\in\{9,10\}
}
\]
from the established general results.


::: pf-proof

The binary expansion
\[
7=111_2
\]
has
\[
\alpha(7)=3.
\]
Step <1>1 gives
\[
N(7)>4\cdot7-2\cdot3=22,
\]
so
\[
N(7)\ge23.
\]
Since $7$ is odd, step <1>2 gives
\[
N(7)
\le
4\cdot7-3-1
=
24.
\]
Thus
\[
N(7)\in\{23,24\}.
\]
This same unresolved two-value range is recorded explicitly in the modern
embedding-dimension literature; see González--Landweber--Shimkus,
*On the embedding dimension of 2-torsion lens spaces*,
Homology Homotopy Appl. 11 (2009), §6.

:::

:::

::: pf-step

Consequently the literal request to “find the smallest $k$” for
arbitrary $n$ has no single presently established formula.


::: pf-proof

Steps <1>4--<1>6 show that exact values are known in substantial families,
but step <1>7 exhibits a value of $n$ for which the cited general embedding
theorems leave two possibilities. Therefore replacing the bounds by one
uniform exact expression would assert a theorem stronger than the established
results used here.

:::

:::

::: pf-qed

The mathematically correct answer is therefore the invariant
\[
k_{\min}(n)=N(n)-2n
\]
with the bounds in step <1>3 and the exact special families in
steps <1>4--<1>6; the source problem is too strong as a request for a general
closed formula.

:::

:::
