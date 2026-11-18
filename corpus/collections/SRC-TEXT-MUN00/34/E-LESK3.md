---
schema: qual/card@1
id: E-LESK3
kind: problem
title: Strong hypotheses short of metrizability
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S34.pdf, Exercise 34.2, page 1 of the file
    (tmp/sources/munkres-solutions-poulsen-S34.pdf, Internet Archive snapshot 20180827202044),
    checked against Munkres, Topology (2000), Section 34 Exercise 2, printed p. 218, Example 3 of
    Section 30 (printed p. 192) and Exercise 30.6. Its example is the Sorgenfrey line, and its
    list of properties is the card's: completely normal, first countable, Lindelof, separable, and
    not metrizable. What was corrected: Moller gives "completely normal [Ex 32.4]", and Exercise
    32.4 is the normality of regular Lindelof spaces; the complete normality of R_l is Exercise
    32.7(g), and the card now cites it, having previously justified it by a hereditary-Lindelof
    argument that is no longer on E-RIGIX.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the five properties into numbered steps and repaired two things while doing so. The
    hereditary Lindelof claim was dropped from the argument: the exercise needs Lindelof, and
    Munkres states that R_l is Lindelof in Example 4 of Section 30 (read in the retained text), which
    is now the citation, whereas the hereditary strengthening is a further theorem that the card did
    not prove and does not use; it is recorded as a remark and marked as not proved here. The
    non-metrizability argument is now a step with its own proof: a basis element of R_l containing x
    and lying inside [x, x+1) must have left endpoint exactly x, so the basis elements attached to
    distinct points are distinct, giving uncountably many; with separability this contradicts
    Exercise 30.5, which says separable metrizable spaces are second countable. The complete
    normality remains a citation to Exercise 32.7(g) as the earlier reading recorded it, not re-read.
---

::: {.exercise}

Give an example showing that a space can be completely normal, and satisfy the first countability axiom, the Lindelöf condition, and have a countable dense subset, and still not be metrizable.
:::

::: {.solution}

The example is the one **Jesper Michael Moller**, *Solutions to exercises in Munkres*, S34 Exercise 34.2, page 1 of that file (`tmp/sources/munkres-solutions-poulsen-S34.pdf`) gives, namely the Sorgenfrey line; the list of properties is the card's, and the arguments for first countability, separability and non-metrizability are written out below. The statement was checked against Munkres, *Topology* (2000), §34 Exercise 2, printed p. 218.

The Sorgenfrey line $\RR_{\ell}$ is $\RR$ with the topology having as basis the half-open intervals $[a,b)$ with $a<b$.

::: pf

::: {.pf-step #first}
$\RR_{\ell}$ is first countable.

::: pf-proof
At $x$ the family $\{[x,x+1/n)\mid n\geq1\}$ is countable, each member is a basis element containing $x$, and any basis element $[a,b)$ containing $x$ satisfies $a\leq x<b$, so $1/n<b-x$ gives $[x,x+1/n)\subset[a,b)$. Hence every neighbourhood of $x$ contains a member of the family.
:::

:::

::: {.pf-step #lindelof}
$\RR_{\ell}$ is Lindelöf.

::: pf-proof
This is stated by Munkres in Example 4 of §30 (printed p. 192), where $\RR_{\ell}$ is used as an example of a Lindelöf space whose square is not Lindelöf. The card cites it rather than reproving it. The stronger statement that every subspace of $\RR_{\ell}$ is Lindelöf is also true but is neither proved here nor needed for the exercise.
:::

:::

::: {.pf-step #separable}
$\RR_{\ell}$ is separable.

::: pf-proof
$\QQ$ is countable and meets every nonempty basis element: if $[a,b)$ is nonempty then $a<b$ and the interval $(a,b)$ contains a rational $q$, which then lies in $[a,b)$. A set meeting every basis element meets every nonempty open set, so $\QQ$ is dense.
:::

:::

::: {.pf-step #not-second}
$\RR_{\ell}$ is not second countable.

::: pf-proof
Let $\mathcal{B}$ be a basis. For each real $x$ choose $B_{x}\in\mathcal{B}$ with $x\in B_{x}\subset[x,x+1)$; such a $B_{x}$ exists because $[x,x+1)$ is a neighbourhood of $x$. A basis element of $\RR_{\ell}$ is a half-open interval $[a,b)$, and $x\in[a,b)\subset[x,x+1)$ forces $x\geq a$ (as $x\in[a,b)$) and $a\geq x$ (as $a\in[a,b)\subset[x,x+1)$), hence $a=x$. So $B_{x}$ has left endpoint $x$, and for $x\neq y$ the sets $B_{x}$ and $B_{y}$ have different left endpoints and are distinct. The map $x\mapsto B_{x}$ is therefore injective from $\RR$ into $\mathcal{B}$, so $\mathcal{B}$ is uncountable.
:::

:::

::: {.pf-step #not-metrizable}
$\RR_{\ell}$ is not metrizable.

::: pf-proof
If $\RR_{\ell}$ were metrizable, then as a separable space it would be second countable: Munkres announces in §30, reference to Exercise 5 of that section, that for metrizable spaces separability and second countability are equivalent. Steps [](#separable){.pf-ref} and [](#not-second){.pf-ref} contradict this.
:::

:::

::: {.pf-step #normal}
$\RR_{\ell}$ is completely normal.

::: pf-proof
This is Exercise 32.7(g) of Munkres, as the earlier reading recorded: every pair of separated subsets of $\RR_{\ell}$ has disjoint neighbourhoods, built from the basis of half-open intervals. The card cites the exercise rather than reproving it.
:::

:::

::: {.pf-step}
The Sorgenfrey line is completely normal, first countable, Lindelöf and separable, and is not metrizable; so the hypotheses listed in the exercise do not force metrizability.

::: pf-proof
Steps [](#normal){.pf-ref}, [](#first){.pf-ref}, [](#lindelof){.pf-ref}, [](#separable){.pf-ref} give the four properties and step [](#not-metrizable){.pf-ref} the failure of metrizability, which is what the exercise asks for.
:::

:::

:::

:::
