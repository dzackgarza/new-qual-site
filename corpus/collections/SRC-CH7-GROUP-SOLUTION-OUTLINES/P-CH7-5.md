---
schema: qual/card@1
id: P-CH7-5
kind: problem
title: Equality of cosets of $3\ZZ$ in $\ZZ$
classification:
  areas: [algebra]
  topics:
    - Cosets and Lagrange's Theorem
relations: []
review: draft
audit:
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Stated the subgroup H of Exercise 3 and moved the three coset pairs out of the solution block into the statement, per page 1 of Ch7Sltns.pdf.
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Structured into Lamport steps from the card's own prose, which is kept as the argument and
      cleaned of extraction formatting (raw Unicode minus signs, spaced LaTeX). Every claim of the
      prose is now a numbered step with its justification; nothing in the mathematics was changed.
      The statement is unchanged, and the card says the argument is its own because no retained
      solution set in the checkout covers this chapter of Gallian.
  - event: source-corrected
    by: claude
    date: 2026-11-19
    note: >-
      The card said the retained solution material in the checkout covers Chapter 8 and the book
      and not this chapter's solutions, and that is false: the collection's own outline is
      retained as `assets/attachments/Ch7Sltns.pdf`, and its entry "# 5" on PDF p. 1 is this
      exercise, with the coset criterion and the same three answers. The rendered sentence now
      cites it and says what the card adds. Found by screening the residue's absence claims
      against the retained attachments; no step of the proof changed.
---

::: {.problem}
Let $H = \{0, \pm 3, \pm 6, \pm 9, \ldots\}$ be as in Exercise 3. Decide whether or not the following cosets of $H$ are the same.

(a) $11 + H$ and $17 + H$.

(b) $-1 + H$ and $5 + H$.

(c) $7 + H$ and $23 + H$.
:::

::: {.solution}
Write the additive group $\ZZ$ and $H=3\ZZ=\{0,\pm3,\pm6,\pm9,\dots\}$. Two cosets coincide exactly when the difference of their representatives lies in $H$, and by Lagrange's theorem the cosets of $H$ are the three residue classes modulo $3$. Each pair below is decided by that criterion alone. The collection retains its solution outline as `assets/attachments/Ch7Sltns.pdf`, whose entry "# 5" on PDF p. 1 is this exercise: it states the criterion $a+H=b+H$ exactly when $b-a\in H$ and applies it to the three pairs, answering yes, yes and no. The card proves that criterion in additive notation and decides each pair with it; the wording is its own.

::: pf

::: {.pf-step #criterion}
For $a,b\in\ZZ$ and a subgroup $H\le\ZZ$, $a+H=b+H$ if and only if $b-a\in H$.

::: pf-proof
If $a+H=b+H$ then $b=b+0\in b+H=a+H$, so $b=a+h$ for some $h\in H$ and $b-a=h\in H$. Conversely, if $b-a=h\in H$, then $b=a+h$ and for any $h'\in H$ one has $b+h'=a+(h+h')\in a+H$, so $b+H\subseteq a+H$; symmetrically $a=b+(-h)$ gives $a+H\subseteq b+H$.
:::

:::


::: {.pf-step #H}
$H=3\ZZ$ is a subgroup of $(\ZZ,+)$ whose cosets are the residue classes modulo $3$.

::: pf-proof
$H$ is the set of integer multiples of $3$, which is closed under addition, contains $0$, and contains $-3n$ whenever it contains $3n$. In additive notation its cosets are the sets $a+H=\{a+3n:n\in\ZZ\}$, which is the congruence class of $a$ modulo $3$, and two integers lie in the same such class exactly when their difference is divisible by $3$, i.e. lies in $H$, which is step [](#criterion){.pf-ref} again.
:::

:::


::: {.pf-step #a}
(a) $11+H=17+H$.

::: pf-proof
$17-11=6=3\cdot2\in H$, so step [](#criterion){.pf-ref} applies with $a=11$, $b=17$. Equivalently $11\equiv17\equiv2\pmod3$.
:::

:::


::: {.pf-step #b}
(b) $-1+H=5+H$.

::: pf-proof
$5-(-1)=6\in H$, so step [](#criterion){.pf-ref} applies with $a=-1$, $b=5$. Equivalently $-1\equiv5\equiv2\pmod3$.
:::

:::


::: {.pf-step #c}
(c) $7+H\ne23+H$.

::: pf-proof
$23-7=16$, and $16$ is not a multiple of $3$ since $16=3\cdot5+1$; so $16\notin H$ and step [](#criterion){.pf-ref} gives $7+H\ne23+H$. Equivalently $7\equiv1$ and $23\equiv2$ modulo $3$, which are different residue classes.
:::

:::


::: {.pf-step #conclusion}
Exactly the pairs in (a) and (b) are equal, and the pair in (c) is not.

::: pf-proof
Steps [](#a){.pf-ref}, [](#b){.pf-ref} and [](#c){.pf-ref} decide the three pairs, and there are no others in the statement.
:::

:::

:::
:::
