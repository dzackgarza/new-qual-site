---
title: What is a scheme
order: 1
topics:
- Schemes
- Spec
- Affine Schemes
---

# What is a scheme

[[D-VKR54]]

[[D-AN662]]

## Why the definition is shaped that way

Points are prime ideals because the preimage of a prime ideal under a ring map $\varphi\colon A\to B$ is prime, so $\mathfrak q\mapsto\varphi^{-1}(\mathfrak q)$ is a continuous map $\Spec B\to\Spec A$; the preimage of a maximal ideal need not be maximal, as $(0)\subset\QQ$ pulls back to $(0)\subset\ZZ$.
The structure sheaf is defined by a local condition so that its sections over $D_f$ come out as $A_f$.
Morphisms are local on stalks so that $\Hom(\Spec B,\Spec A)=\Hom(A,B)$.

[[FE-O12TX]]

## Recognising an affine scheme

[[T-SK599]]

By [[algebraic-geometry/cohomology/vanishing-and-duality|Serre's criterion]], a noetherian scheme $X$ is affine exactly when $H^1(X,\mci)=0$ for every coherent ideal sheaf $\mci\subseteq\OO_X$.

## Covers of an affine scheme

[[PR-SCHUNITCOVER]]

## Formal schemes

[[D-SCHFORMAL]]

## Checking a property on one affine cover

[[T-AFFCOMM]]
