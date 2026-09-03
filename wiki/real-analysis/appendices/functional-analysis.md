---
title: "Appendix: Functional Analysis"
order: 33
---

# Appendix: Functional Analysis

The Banach-space theorems split into two groups.
Open mapping, bounded inverse, and closed graph are three faces of the same completeness phenomenon for a single linear operator.
Uniform boundedness controls an entire family of operators.
Hahn--Banach is different: it is an extension/separation theorem and does not require completeness.

## Open mapping, bounded inverse, and closed graph

Let $X,Y$ be Banach spaces.
A bounded surjective linear map $T:X\to Y$ is open; hence a bounded bijection has bounded inverse.
Equivalently in the form used for operators, an everywhere-defined linear map $T:X\to Y$ whose graph is closed must be bounded.
When a problem asks you to prove continuity without an estimate, check whether one of these qualitative hypotheses is easier to verify than $\|Tx\|\le C\|x\|$ directly.

[[T-FO27T]]

[[T-KQTPR]]

[[T-TTLXS]]

## Uniform boundedness

For a family of bounded linear maps $T_\alpha:X\to Y$ with $X$ Banach, pointwise boundedness—$\sup_\alpha\|T_\alpha x\|<\infty$ for every fixed $x$—forces a uniform operator-norm bound $\sup_\alpha\|T_\alpha\|<\infty$.
The quantifier swap is the whole theorem; it is the standard contradiction tool when operator norms are suspected to blow up.

[[T-F2THV]]

[[FT-JRRRW]] [[FF-YJXMF]]

## Hahn--Banach

Hahn--Banach extends a bounded linear functional from a subspace without increasing its norm.
Its practical consequences are separation and norm detection: for nonzero $x$ one can find a continuous functional attaining $\|x\|$ on $x$ after normalization.
Unlike the three Banach-space isomorphism theorems above, the extension principle is not a completeness statement.

[[T-OW2QG]]

[[FF-7NXLO]]
