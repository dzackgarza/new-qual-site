---
schema: qual/card@1
id: P-BKF10-7B
kind: problem
title: The derivative bound $\abs{ f'(0)}\le1$ in Schwarz's lemma
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 7B, printed pp. 6--7 of the packet is the source of the argument, and the paragraph at the head
    of the solution says what the card adds. Checked: the packet read in its text layer at the page
    named and the card's steps compared with its sentences, `qualc.authoring check` on the card, and
    `tmp/lam.sh` for the numbering and the QED. Not checked: no other card of the collection in this
    pass.
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 7B of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the removable extension of f(z)/z, maximum modulus on every
    smaller disk, and the limiting radius argument.
---

::: {.problem}
If $f$ is analytic from the unit disk into itself and $f(0)=0$, prove that
$$
\abs{f'(0)}\le1.
$$
Since this problem is part of the proof of Schwarz's lemma, quoting that lemma does not receive full credit.
:::

::: {.solution}

The argument is Problem 7B of the retained Berkeley preliminary-exam solution packet, `assets/attachments/f10solutions.pdf`, printed pp. 6--7 of that file, transcribed: put $g=f/z$, so that the claim is $\abs{g(0)}\le1$; by the maximum modulus principle $\abs{g(0)}$ is at most the maximum of $\abs{g}$ on the circle of radius $1-\varepsilon$, which is at most $1/(1-\varepsilon)$ because $\abs{f}\le1$ and $\abs{1/z}\le1/(1-\varepsilon)$; and $\varepsilon>0$ is arbitrary. The card adds the removal of the singularity at $0$, which makes $g$ analytic on the disc, and the step structure.
Let
$$
D\coloneqq\{z\in\CC:\abs{z}<1\}.
$$

::: pf

::: {.pf-step #s1}

The function
$$
g(z)\coloneqq
\begin{cases}
\dfrac{f(z)}z,&z\ne0,\\[4pt]
f'(0),&z=0
\end{cases}
$$
is analytic on $D$.

::: pf-proof

Since $f(0)=0$ and $f$ is analytic,
$$
\lim_{z\to0}\frac{f(z)}z
=\lim_{z\to0}\frac{f(z)-f(0)}{z-0}
=f'(0).
$$
Thus $f(z)/z$ has a removable singularity at $0$, and the displayed
value $g(0)=f'(0)$ gives its analytic extension to all of $D$.

:::

:::

::: {.pf-step #s2}

For every $0<r<1$,
$$
\abs{g(0)}\le\frac1r.
$$

::: pf-proof

On the circle $\abs{z}=r$, the hypothesis that $f(D)\subseteq D$ gives
$$
\abs{f(z)}<1.
$$
Therefore
$$
\abs{g(z)}=\frac{\abs{f(z)}}r\le\frac1r.
$$
By step [](#s1){.pf-ref}, $g$ is analytic on a neighborhood of the closed disk
$\abs{z}\le r$. The maximum modulus principle therefore gives
$$
\abs{g(0)}
\le\max_{\abs{z}=r}\abs{g(z)}
\le\frac1r.
$$

:::

:::

::: {.pf-step #s3}

One has
$$
\abs{f'(0)}\le1.
$$

::: pf-proof

By definition in step [](#s1){.pf-ref},
$$
\abs{f'(0)}=\abs{g(0)}.
$$
Step [](#s2){.pf-ref} gives $\abs{g(0)}\le1/r$ for every $0<r<1$. Letting
$r\to1^-$ yields
$$
\abs{f'(0)}\le1.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required derivative bound.

:::

:::

:::
