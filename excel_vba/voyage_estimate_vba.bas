Attribute VB_Name = "VoyageEstimateModule"
Option Explicit

' Simplified VBA version of the voyage estimate model.
' This code can be imported into an Excel macro-enabled workbook (.xlsm).

Sub RunVoyageEstimate()
    Dim freightRevenue As Double
    Dim seaDays As Double
    Dim portDays As Double
    Dim dailyConsumption As Double
    Dim bunkerPrice As Double
    Dim portCosts As Double
    Dim canalCosts As Double
    Dim otherCosts As Double
    Dim commissionRate As Double
    
    Dim totalDays As Double
    Dim bunkerCost As Double
    Dim commission As Double
    Dim totalCosts As Double
    Dim profitLoss As Double
    Dim tce As Double
    
    ' Example input cells. Adjust to your Excel template.
    freightRevenue = Range("B2").Value
    seaDays = Range("B3").Value
    portDays = Range("B4").Value
    dailyConsumption = Range("B5").Value
    bunkerPrice = Range("B6").Value
    portCosts = Range("B7").Value
    canalCosts = Range("B8").Value
    otherCosts = Range("B9").Value
    commissionRate = Range("B10").Value
    
    totalDays = seaDays + portDays
    bunkerCost = seaDays * dailyConsumption * bunkerPrice
    commission = freightRevenue * commissionRate
    totalCosts = bunkerCost + portCosts + canalCosts + otherCosts + commission
    profitLoss = freightRevenue - totalCosts
    
    If totalDays <> 0 Then
        tce = profitLoss / totalDays
    Else
        tce = 0
    End If
    
    ' Example output cells.
    Range("E2").Value = totalDays
    Range("E3").Value = bunkerCost
    Range("E4").Value = commission
    Range("E5").Value = totalCosts
    Range("E6").Value = profitLoss
    Range("E7").Value = tce
    
    MsgBox "Voyage estimate completed.", vbInformation
End Sub
