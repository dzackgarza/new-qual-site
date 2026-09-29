---
schema: qual/card@1
id: P-AMD-OXM52UGE
kind: problem
title: The homophony group is trivial
classification:
  areas:
  - topology
  topics:
  - Group Presentations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---
::: {.problem}
Prove that the homophony group is trivial.
:::

::: {.solution}
Let $H$ be the quotient of the free group on the $26$ letters by the relations $w_1=w_2$ whenever the two English words $w_1,w_2$ are homophones. We show each letter is the identity. The elimination below is the classical proof of Mestre--Schoof--Washington--Zagier; every step is an ordinary left/right cancellation in the group after previously eliminated letters are set equal to $1$.

::: pf

::: {.pf-step #s1}

First eliminate the vowels and semivowels
$$
e,a,i,o,u,w,y.
$$

::: pf-proof

The homophone relation $\text{bye}=\text{by}$ gives
$$
bye=by\quad\Longrightarrow\quad e=1
$$
by left cancellation of the common prefix $by$.
Then
$$
\begin{array}{rcl}
\text{lead}=\text{led}&\Longrightarrow&a=1,\\
\text{maid}=\text{made}&\Longrightarrow&i=1,\\
\text{sow}=\text{sew}&\Longrightarrow&o=1,\\
\text{buy}=\text{by}&\Longrightarrow&u=1,\\
\text{sow}=\text{so}&\Longrightarrow&w=1,\\
\text{lye}=\text{lie}&\Longrightarrow&y=1.
\end{array}
$$
For example, after $e=1$, the first relation becomes $lad=ld$, so cancellation of $l$ on the left and $d$ on the right gives $a=1$. The others are identical cancellation arguments using letters already eliminated earlier in the displayed order.

:::

:::

::: {.pf-step #s2}

Next eliminate
$$
h,k,n,p,b.
$$

::: pf-proof

Using the relations
$$
\text{hour}=\text{our},\qquad
\text{knight}=\text{night},\qquad
\text{damn}=\text{dam},\qquad
\text{psalter}=\text{salter},\qquad
\text{plumb}=\text{plum},
$$
we obtain respectively $h=k=n=p=b=1$. Each equality has the form $u\ell v=uv$ after the letters from step [](#s1){.pf-ref} and the previously eliminated letters are removed, so cancellation gives $\ell=1$.

:::

:::

::: {.pf-step #s3}

Next eliminate
$$
s,t,l,r,m.
$$

::: pf-proof

The homophone relations
$$
\text{bass}=\text{base},\quad
\text{butt}=\text{but},\quad
\text{tolled}=\text{told},\quad
\text{barred}=\text{bard},\quad
\text{dammed}=\text{damned}
$$
reduce, using the letters already known to be trivial, to
$$
s^2=s,\qquad t^2=t,\qquad l^2=l,\qquad r^2=r,\qquad m^2=m.
$$
In a group an idempotent element is the identity: $x^2=x$ implies $x=1$ after multiplying by $x^{-1}$. Hence $s=t=l=r=m=1$.

:::

:::

::: {.pf-step #s4}

Eliminate $d$ and $g$.

::: pf-proof

The relations
$$
\text{chased}=\text{chaste},\qquad
\text{sign}=\text{sine}
$$
reduce, after the previous eliminations, to $d=1$ and $g=1$ respectively.

:::

:::

::: {.pf-step #s5}

Eliminate
$$
z,c,j,q,x.
$$

::: pf-proof

The homophone relations
$$
\text{daze}=\text{days},\qquad
\text{cite}=\text{sight},\qquad
\text{jeans}=\text{genes},\qquad
\text{queue}=\text{cue},\qquad
\text{tax}=\text{tacks}
$$
reduce successively to
$$
z=1,\qquad c=1,\qquad j=1,\qquad q=1,\qquad x=1,
$$
using only letters already eliminated before the relevant step.

:::

:::

::: {.pf-step #s6}

Finally eliminate $f$ and $v$.

::: pf-proof

The relation $\text{phase}=\text{faze}$ reduces to $f=1$ because $p,h,a,s,e,z$ are already trivial. Then
$$
\text{chivvy}=\text{chivy}
$$
reduces to $v^2=v$, hence $v=1$.

:::

:::

::: pf-step

Therefore every one of the $26$ generators is trivial, so
$$
\boxed{H=1}.
$$

::: pf-proof

The letters eliminated in steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} are
$$
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
$$
which is the complete generating set.

:::

:::

:::

:::
