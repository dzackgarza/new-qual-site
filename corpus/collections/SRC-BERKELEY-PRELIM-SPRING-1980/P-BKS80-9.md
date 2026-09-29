---
schema: qual/card@1
id: P-BKS80-9
kind: problem
title: Centralizer of an explicit real $2\times2$ matrix
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction loses part of the displayed 2-by-2 matrix A. It preserves entries 1, 2, and 3 but not enough layout to recover the fourth entry safely. An archival Berkeley problem compilation reproduces the same problem but likewise drops the display, so the missing matrix is not guessed here.
- event: source-corrected
  by: chatgpt
  date: 2026-09-24
  note: Direct inspection of page 2 of the retained source PDF confirms that A has rows (1,2) and (3,4).
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked all four entrywise commutation equations and the reparameterization B=sI+tA.
---

::: {.problem}
Let
\[
A=
\begin{pmatrix}
1&2\\
3&4
\end{pmatrix}.
\]
Show that every real matrix $B$ satisfying
\[
AB=BA
\]
has the form
\[
B=sI+tA
\]
for some $s,t\in\RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Write
$$
B=
\begin{pmatrix}
p&q\\
r&u
\end{pmatrix}.
$$
Then $AB=BA$ is equivalent to
$$
2r=3q,
\qquad
2(u-p)=3q.
$$

::: pf-proof

Direct multiplication gives
$$
AB
=
\begin{pmatrix}
p+2r&q+2u\\
3p+4r&3q+4u
\end{pmatrix}
$$
and
$$
BA
=
\begin{pmatrix}
p+3q&2p+4q\\
r+3u&2r+4u
\end{pmatrix}.
$$
Equating the $(1,1)$ and $(2,2)$ entries gives
$$
2r=3q.
$$
Equating the $(1,2)$ entries gives
$$
2(u-p)=3q.
$$
The $(2,1)$ equation is then the same relation, since it reads
$$
3p+3r=3u.
$$
Thus the two displayed equations are equivalent to all four entrywise
conditions.

:::

:::

::: {.pf-step #s2}

Every matrix $B$ commuting with $A$ has the form
$$
B=sI+tA
$$
for real $s,t$.

::: pf-proof

By step [](#s1){.pf-ref}, put
$$
t\coloneqq\frac q2.
$$
Then
$$
r=3t,
\qquad
u-p=3t.
$$
Set
$$
s\coloneqq p-t.
$$
Since $q=2t$ and $u=p+3t=s+4t$, one has
$$
B
=
\begin{pmatrix}
s+t&2t\\
3t&s+4t
\end{pmatrix}
=
sI+t
\begin{pmatrix}
1&2\\
3&4
\end{pmatrix}
=
sI+tA.
$$

:::

:::

::: {.pf-step #s3}

Conversely, every matrix $sI+tA$ commutes with $A$.

::: pf-proof

For $s,t\in\RR$,
$$
A(sI+tA)=sA+tA^2=(sI+tA)A.
$$

:::

:::

::: {.pf-step #s4}

Hence the full real centralizer of $A$ is
$$
\boxed{\{sI+tA:s,t\in\RR\}.}
$$

::: pf-proof

Step [](#s2){.pf-ref} proves containment of the centralizer in the displayed set, and
step [](#s3){.pf-ref} proves the reverse containment.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} contains the required assertion.

:::

:::

:::
