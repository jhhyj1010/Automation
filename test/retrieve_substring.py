#!/usr/bin/env python3
import re, os

s = "### :bangbang: Your action is required\n\nRestricted governance requires complete and thoughtful answers to the questions below, based on the letter and spirit of [this documentation](https://1source.intel.com/docs/overview/organizations_intel_restricted). Click on the top-right side of this comment and select the Edit option to add your responses.\n\n:warning: Do not share any Intel Top Secret information\n\n---\n\n### What is the content?\n\nDescribe your content in simple terms. What does it do? Expand acronyms, please.\n\n### Why should it be restricted?\n\nWhat makes this content require a restricted repository? Where applicable, **provide one or more of the justifications documented [here](https://1source.intel.com/docs/overview/organizations_intel_restricted#criteria-that-qualifies-the-code-to-be-in-a-restricted-repository)**.\n\n### Diligence done?\n\nWhat senior technical leaders, senior managers, security experts, and/or legal experts have you consulted with?  If the justification is third-party restricted IP, provide a copy of the explicit disclosure restrictions from the NDA or similar legal document.\n\n### Impact\n\nWhat is the impact to Intel's 1SCM/innersource culture and vision if this content is restricted? What information will others at Intel not have as reference to accelerate their development and validation?  (Do not simply restate your justification to restrict the content.)\n\n### Architecture\n\nRestricted repositories should be used to restricted the minimum possible amount of IP whenever feasible. Is/Can your content be architected to achieve that goal?\n\nCan you re-architect/reorganize your content in the future, if necessary, to get closer to that goal?\n"
s0 = 'Can your content be architected to achieve that goal?'
s1 = re.match(r'Can (.*) goal?', s, re.M|re.I).group(1)
print(s1)
def get_content_between_substrings(content, start_substring, end_substring):
    start = content.find(start_substring) + len(start_substring)
    end = content.find(end_substring, start)
    if start - len(start_substring) != -1 and end != -1:
        return content[start:end].strip()
    else:
        return "Substrings not found in the content"

s2 = get_content_between_substrings(s, 'What is the content?', '### Why should it be restricted?')
print(s2)
