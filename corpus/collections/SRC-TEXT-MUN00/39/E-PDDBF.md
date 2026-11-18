---
schema: qual/card@1
id: E-PDDBF
kind: problem
title: A point-finite open covering that is not locally finite
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 39 Exercise 2, printed p. 247, with the definitions of point-finite and locally finite, and the fact that $1/n\to0$. No correction was needed.
---

::: {.exercise}

Find a point-finite open covering $\mathcal{A}$ of $\RR$ that is not locally finite.
(The collection $\mathcal{A}$ is point-finite if each point of $\RR$ lies in only finitely many elements of $\mathcal{A}$.)
:::

::: {.solution}

No retained solution set covers this exercise: the card's audit records that no complete published solution was located, and none is used here, so the construction and its verification are the card's own. The statement was checked against Munkres, *Topology* (2000), §39 Exercise 2, printed p. 248, and the definitions of point-finite and locally finite families are the ones in §39, printed p. 244.

Throughout,
$$
U_{n}\coloneqq\Big(\frac{1}{n+1},\frac{1}{n-1}\Big)\quad(n\geq2),\qquad
\mathcal{A}\coloneqq\theset{(-\infty,1),(0,\infty)}\cup\theset{U_{n}\mid n\geq2}.
$$

::: pf

::: {.pf-step #covering}
$\mathcal{A}$ is an open covering of $\RR$.

::: pf-proof
Each $U_{n}$ is an open interval, indeed a nonempty one, and $(-\infty,1)$ and $(0,\infty)$ are open rays. Since $(-\infty,1)\cup(0,\infty)=\RR$, the family covers $\RR$.
:::

:::

::: {.pf-step #point-finite}
$\mathcal{A}$ is point-finite.

:::: pf-proof

::: {.pf-step #nonpositive}
A point $x\leq0$ lies in no $U_{n}$.

::: pf-proof
$U_{n}\subset(0,\infty)$ because $1/(n+1)>0$ for $n\geq2$, so no point of $(-\infty,0]$ belongs to any $U_{n}$.
:::

:::

::: {.pf-step #positive}
A point $x>0$ lies in only finitely many $U_{n}$.

::: pf-proof
Choose $N\geq2$ with $1/(N-1)<x$, possible since $1/(N-1)\to0$. For $n\geq N$ one has $1/(n-1)\leq1/(N-1)<x$, so $x\notin(1/(n+1),1/(n-1))=U_{n}$. Hence $x$ can lie only in $U_{2},\dots,U_{N-1}$.
:::

:::

::: {.pf-step}
Every point of $\RR$ lies in only finitely many members of $\mathcal{A}$.

::: pf-proof
A point lies in at most the two rays together with the finitely many sets allowed by steps [](#nonpositive){.pf-ref} and [](#positive){.pf-ref}, and a finite union of finite collections is finite.
:::

:::

::::

:::

::: {.pf-step #not-locally-finite}
$\mathcal{A}$ is not locally finite at $0$.

:::: pf-proof

::: {.pf-step #meets-U-n}
For every $\varepsilon>0$ the interval $(-\varepsilon,\varepsilon)$ meets $U_{n}$ for all $n$ with $1/n<\varepsilon$.

::: pf-proof
If $1/n<\varepsilon$ and $n\geq2$, then $\frac{1}{n+1}<\frac{1}{n}<\frac{1}{n-1}$, so $\frac{1}{n}\in U_{n}$, and also $\frac{1}{n}<\varepsilon$ with $\frac{1}{n}>0$, so $\frac{1}{n}\in(-\varepsilon,\varepsilon)$. Hence that point lies in the intersection.
:::

:::

::: {.pf-step #no-small-neighbourhood}
No neighbourhood of $0$ meets only finitely many members of $\mathcal{A}$.

::: pf-proof
A neighbourhood $W$ of $0$ contains an interval $(-\varepsilon,\varepsilon)$ with $\varepsilon>0$, and by step [](#meets-U-n){.pf-ref} it meets $U_{n}$ for every $n>1/\varepsilon$, of which there are infinitely many; so $W$ meets infinitely many members of $\mathcal{A}$.
:::

:::

::::

:::

::: pf-step
Therefore $\mathcal{A}$ is a point-finite open covering of $\RR$ that is not locally finite.

::: pf-proof
$\mathcal{A}$ is an open covering by step [](#covering){.pf-ref} and point-finite by step [](#point-finite){.pf-ref}; a family is locally finite when every point has a neighbourhood meeting only finitely many of its members, and the point $0$ has no such neighbourhood by step [](#not-locally-finite){.pf-ref}. Hence the covering is point-finite but not locally finite, which is what the exercise asks for.
:::

:::

:::

:::
