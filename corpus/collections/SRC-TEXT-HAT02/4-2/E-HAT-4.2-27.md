---
schema: qual/card@1
id: E-HAT-4.2-27
kind: problem
title: "Image of $\\pi_2(X) \\to \\pi_2(X,A)$ is central"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 27; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above, which is correct as it
    stood: exactness gives $\partial a=0$, Lemma 4.39 gives $a+b-a=(\partial a)b$, and the
    trivial action gives $b$. Added: the hypothesis that $\pi_2(X,A,x_0)$ is a group with a
    $\pi_1(A)$-action and is not assumed abelian, and the explicit appeal to exactness at
    $\pi_2(X,A,x_0)$ of the sequence on printed p. 344. Cited: Lemma 4.39 on printed p. 373,
    the exercise on printed p. 391. Not claimed: a retained solution set, so the argument is
    the card's own.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Correction to this date's earlier note, from a search of the retained sets after the
    proof was written. The card said no retained solution set covers the exercise; Steven
    V. Sam's set does, at Exercise 4.2.27, PDF p. 24, and the UCR Math 205B help file
    repeats the same text, so there are two retained copies. The argument on the card is
    that argument, cited there; the card's own addition is only the exactness and action
    bookkeeping. Mathematics unchanged and re-read; the exercise is on printed p. 391.
---

::: {.problem}
Show that the image of the map $\pi_2(X, x_0) \to \pi_2(X, A, x_0)$ lies in the center of $\pi_2(X, A, x_0)$. (This exercise should be in §4.1.)
:::

::: {.solution}
The published solution is **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), Exercise 4.2.27**, whose argument this is verbatim in substance: the image is the kernel of $\partial$ by exactness, and Lemma 4.39 gives $xbx^{-1}=e$ for $x$ in that kernel. The card adds only the bookkeeping — that the action of $\partial x=0$ is trivial and that the resulting identity is $x+b=b+x$ in a group not assumed abelian. The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 27, with the parenthetical remark the book prints beside it, and Lemma 4.39 is printed on p. 373.

Throughout $(X,A,x_0)$ is a pointed pair with $A\subset X$, $j:(X,x_0)\to(X,A)$ the inclusion of pairs, and $\partial:\pi_2(X,A,x_0)\to\pi_1(A,x_0)$ the boundary map of the long exact sequence. The set $\pi_2(X,A,x_0)$ is a group, written additively but not assumed abelian, on which $\pi_1(A,x_0)$ acts, and $\pi_2(X,x_0)$ is abelian.

::: pf

::: {.pf-step #exactness}
If $a=j_*(\tilde a)$ for some $\tilde a\in\pi_2(X,x_0)$, then $\partial a=0$.

::: pf-proof
The long exact sequence of the pair (printed p. 344) is exact at $\pi_2(X,A,x_0)$, so $\operatorname{im}j_*=\ker\partial$. Hence $\partial a=\partial j_*\tilde a=0$ by exactness and the chain property $\partial\circ j_*=0$.

:::

:::

::: {.pf-step #lemma}
For all $a,b\in\pi_2(X,A,x_0)$, the identity $a+b-a=(\partial a)b$ holds, where $(\partial a)b$ is the action of the element $\partial a\in\pi_1(A,x_0)$ on $b$.

::: pf-proof
This is Lemma 4.39, obtained by an explicit homotopy from $a+b-a$ to $(\partial a)b$ carried by the boundary circle of the class $a$.

:::

:::

::: {.pf-step #commutes}
Every $a\in\operatorname{im}j_*$ commutes with every $b\in\pi_2(X,A,x_0)$.

::: pf-proof
Fix $b$ and write $a=j_*(\tilde a)$. By step [](#exactness){.pf-ref}, $\partial a=0$, so the action of $\partial a$ on $b$ is the trivial action and $(\partial a)b=b$. Step [](#lemma){.pf-ref} then gives $a+b-a=b$. Adding $a$ on the right in the group $\pi_2(X,A,x_0)$ gives $a+b=b+a$.

:::

:::

::: {.pf-step #conclusion}
$\operatorname{im}\bigl(j_*:\pi_2(X,x_0)\to\pi_2(X,A,x_0)\bigr)\subset Z\bigl(\pi_2(X,A,x_0)\bigr)$.

::: pf-proof
Step [](#commutes){.pf-ref} says precisely that each element of the image commutes with every element of the group, which is the definition of the centre.

:::

:::

:::
:::
