---
schema: qual/card@1
id: D-VK2KZ
kind: definition
title: Discrete valuation ring
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Local Rings
  - Principal Ideal Domains
relations: []
review: draft
---

::: {.definition}
A \dfn{discrete valuation ring}, or \dfn{DVR}, is a [[D-HTIL5|principal ideal domain]] that is a [[D-TGB4R|local ring]] and is not a field.
:::

::: {.proposition}
An integral domain $R$ with fraction field $K$ is a discrete valuation ring if and only if it is the [[D-HWLVG|valuation ring]] $\theset{x\in K^\times\st v(x)\ge0}\cup\theset{0}$ of a discrete valuation $v\colon K^\times\to\ZZ$.
An element $\pi$ with $v(\pi)=1$ is a \dfn{uniformizer}: it generates the maximal ideal, and every nonzero $x\in K$ is $u\pi^{v(x)}$ for a unit $u\in R^\times$.
[@AM18, Chapter 9]
:::
