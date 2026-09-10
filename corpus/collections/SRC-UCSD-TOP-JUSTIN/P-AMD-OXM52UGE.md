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

<1>1. First eliminate the vowels and semivowels
$$
e,a,i,o,u,w,y.
$$
::: {.proof}
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

<1>2. Next eliminate
$$
h,k,n,p,b.
$$
::: {.proof}
Using the relations
$$
\text{hour}=\text{our},\qquad
\text{knight}=\text{night},\qquad
\text{damn}=\text{dam},\qquad
\text{psalter}=\text{salter},\qquad
\text{plumb}=\text{plum},
$$
we obtain respectively $h=k=n=p=b=1$. Each equality has the form $u\ell v=uv$ after the letters from <1>1 and the previously eliminated letters are removed, so cancellation gives $\ell=1$.
:::

<1>3. Next eliminate
$$
s,t,l,r,m.
$$
::: {.proof}
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

<1>4. Eliminate $d$ and $g$.
::: {.proof}
The relations
$$
\text{chased}=\text{chaste},\qquad
\text{sign}=\text{sine}
$$
reduce, after the previous eliminations, to $d=1$ and $g=1$ respectively.
:::

<1>5. Eliminate
$$
z,c,j,q,x.
$$
::: {.proof}
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

<1>6. Finally eliminate $f$ and $v$.
::: {.proof}
The relation $\text{phase}=\text{faze}$ reduces to $f=1$ because $p,h,a,s,e,z$ are already trivial. Then
$$
\text{chivvy}=\text{chivy}
$$
reduces to $v^2=v$, hence $v=1$.
:::

<1>7. Therefore every one of the $26$ generators is trivial, so
$$
\boxed{H=1}.
$$
::: {.proof}
The letters eliminated in <1>1--<1>6 are
$$
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
$$
which is the complete generating set.
:::
:::
 {.proof}
definition of the homophony group.
:::

<1>2. "knight" and "night" are homophones, so $k = e$.
::: {.proof}
the relation $\text{knight} = \text{night}$ cancels the common suffix, leaving $k = e$.
:::

<1>3. "write" and "right" are homophones, so $w = e$.
::: {.proof}
cancelling the common "rite" leaves $w = e$.
:::

<1>4. "see" and "sea" are homophones, and "sea" and "c" are homophones, so $s = e$ and $c = e$.
::: {.proof}
$\text{see} = \text{sea}$ gives $e = a$ (after cancelling $s$ and $e$), and $\text{sea} = c$ gives $s \cdot e \cdot a = c$, so $s = e$ and $c = e$.
:::

<1>5. "you" and "u" are homophones, so $y \cdot o = e$.
::: {.proof}
$\text{you} = u$ cancels the trailing $u$, leaving $y \cdot o = e$.
:::

<1>6. "eye" and "i" are homophones, so $y = i$.
::: {.proof}
$\text{eye} = i$ gives $e \cdot y \cdot e = i$, i.e. $y = i$.
:::

<1>7. "why" and "y" are homophones, so $h = e$.
::: {.proof}
$\text{why} = y$ gives $w \cdot h \cdot y = y$, so $w \cdot h = e$, and $w = e$ by <1>3, hence $h = e$.
:::

<1>8. "are" and "r" are homophones, so $a = e$.
::: {.proof}
$\text{are} = r$ gives $a \cdot r \cdot e = r$, so $a = e$.
:::

<1>9. "queue" and "q" are homophones, so $u = e$.
::: {.proof}
$\text{queue} = q$ gives $q \cdot u \cdot e \cdot u \cdot e = q$, so $u = e$.
:::

<1>10. "jay" and "j" are homophones, so $y = e$.
::: {.proof}
$\text{jay} = j$ gives $j \cdot a \cdot y = j$, so $a \cdot y = e$, and $a = e$ by <1>8, hence $y = e$.
:::

<1>11. "ell" and "l" are homophones, so $l = e$; "eff" and "f" are homophones, so $f = e$.
::: {.proof}
$\text{ell} = l$ gives $e \cdot l \cdot l = l$, so $l = e$; $\text{eff} = f$ gives $e \cdot f \cdot f = f$, so $f = e$.
:::

<1>12. The remaining letters are trivial by their letter-names: "bee" $= b$, "tea" $= t$, "gee" $= g$, "pee" $= p$, "vee" $= v$, "ex" $= x$, "zee" $= z$, "em" $= m$, "en" $= n$, "oh" $= o$, "double-u" $= w$, "aitch" $= h$.
::: {.proof}
each letter-name is a homophone of the letter itself, and the extra letters in each name are already trivial by <1>2–<1>11.
:::

<1>13. Hence every generator of $H$ is trivial, so $H$ is the trivial group.
::: {.proof}
<1>2–<1>12 cover all $26$ letters.
:::

<1>14. Q.E.D.
::: {.proof}
<1>13.
:::
:::
