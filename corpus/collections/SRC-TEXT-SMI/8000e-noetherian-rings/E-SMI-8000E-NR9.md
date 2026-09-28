---
schema: qual/card@1
id: E-SMI-8000E-NR9
kind: problem
title: Extensions of ideals along surjective ring maps
classification:
  areas:
  - algebra
  topics:
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the extension/correspondence statement with the local 8000e PDF and extraction, Noetherian-rings problem 9."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Gave a nonsurjective counterexample, proved image ideals under surjections, and showed extension and contraction are inverse bijections above ker f."
---

::: {.exercise}
If $f: R \to S$ is a ring map and $I$ an ideal of $R$, then $f(I)$ may not be an ideal of $S$.
If $f$ is surjective, $f(I)$ is an ideal of $S$, and sending $I$ to $f(I)$ gives a one-to-one correspondence between ideals $I$ of $R$ containing $\ker f$ and all ideals of $S$.
:::


::: {.solution}
<1>1. Without surjectivity, $f(I)$ need not be an ideal of $S$.
::: {.proof}
Take the inclusion
$$
f:\mathbb Z\hookrightarrow\mathbb Q
$$
and the ideal
$$
I=2\mathbb Z.
$$
Then
$$
f(I)=2\mathbb Z\subseteq\mathbb Q.
$$
This is not an ideal of $\mathbb Q$: it contains $2$, but multiplication by
$1/2\in\mathbb Q$ gives
$$
(1/2)\cdot2=1\notin2\mathbb Z.
$$
:::

<1>2. If $f$ is surjective, then $f(I)$ is an ideal of $S$.
::: {.proof}
The set $f(I)$ is an additive subgroup of $S$. Let
$$
y=f(a)\in f(I)
$$
and let $s\in S$. By surjectivity choose $r\in R$ with
$$
f(r)=s.
$$
Then
$$
sy=f(r)f(a)=f(ra).
$$
Since $a\in I$ and $I$ is an ideal,
$$
ra\in I,
$$
so $sy\in f(I)$. Thus $f(I)$ is an ideal of $S$.
:::

<1>3. Extension followed by contraction recovers every ideal containing $\ker f$.
::: {.proof}
Assume $f$ is surjective and let
$$
I\supseteq\ker f.
$$
Certainly
$$
I\subseteq f^{-1}(f(I)).
$$
Conversely, if $r\in f^{-1}(f(I))$, then
$$
f(r)=f(a)
$$
for some $a\in I$. Hence
$$
f(r-a)=0,
$$
so
$$
r-a\in\ker f\subseteq I.
$$
Since $a\in I$, it follows that $r\in I$. Therefore
$$
\boxed{f^{-1}(f(I))=I.}
$$
:::

<1>4. Contraction followed by extension recovers every ideal of $S$.
::: {.proof}
Let $J\subseteq S$ be an ideal. One inclusion is immediate:
$$
f(f^{-1}(J))\subseteq J.
$$
For the reverse inclusion, if $y\in J$, surjectivity gives $r\in R$ with
$$
f(r)=y.
$$
Then $r\in f^{-1}(J)$, so
$$
y=f(r)\in f(f^{-1}(J)).
$$
Thus
$$
\boxed{f(f^{-1}(J))=J.}
$$
:::

Steps <1>3--<1>4 show that extension and contraction are inverse bijections
between
$$
\{I\triangleleft R:\ker f\subseteq I\}
$$
and the ideals of $S$.
:::
