# Lab‑02 – GuardDuty → EventBridge → SNS

Goal: forward every GuardDuty finding to an SNS topic so Ops/on‑call gets notified.

## Architecture
GuardDuty ▶︎ EventBridge Rule ▶︎ SNS Topic ▶︎ Email

## Steps I followed
1. Created SNS topic **GuardDutyAlerts**, added & confirmed email subscription.  
2. Enabled GuardDuty (free 30‑day trial).  
3. EventBridge rule **GuardDutyToSNS** with pattern  
   ```json
   {
     "source": ["aws.guardduty"],
     "detail-type": ["GuardDuty Finding"]
   }
