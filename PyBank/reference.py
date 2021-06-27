# Sub StockSummary()

#   ' Set Headers
  Cells(1, 9) = "<Ticker>"
  Cells(1, 10) = "<Yearly Change>"
  Cells(1, 11) = "Yearly % Change>"
  Cells(1, 12) = "<Total Volume>"

#   ' Set an initial variable for holding Ticker
  Dim Ticker As String

#   ' Set an initial variable for holding the total volume per each ticker
  Dim Ticker_Total As Double
  Ticker_Total = 0

#   ' Keep track of the location for each Ticker in the summary table
  Dim Summary_Table_Row As Integer
  Summary_Table_Row = 2
  
#   ' Set Lastrow
  Lastrow = Cells(Rows.Count, 1).End(xlUp).Row

#   ' Loop through all Ticker trading days
  For i = 2 To Lastrow

    # ' Check if we are still within the Ticker, if it is not...
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

    #   ' Set the Ticker name
      Ticker = Cells(i, 1).Value

    #   ' Add to the Ticker Total
      Ticker_Total = Ticker_Total + Cells(i, 7).Value

    #   ' Print the Ticker name in the Summary Table
      Range("I" & Summary_Table_Row).Value = Ticker

    #   ' Print the Ticker total amount to the Summary Table
      Range("L" & Summary_Table_Row).Value = Ticker_Total

    #   ' Add one to the summary table row
      Summary_Table_Row = Summary_Table_Row + 1
      
    #   ' Reset the Ticker Total
      Ticker_Total = 0

    # ' If the cell immediately following a row is the same brand...
    Else

    #   ' Add to the Ticker Total
      Ticker_Total = Ticker_Total + Cells(i, 7).Value

    End If

  Next i
  
  Dim Openprice As Double
  Dim Closeprice As Double
  
  
  Lastrow = Cells(Rows.Count, 1).End(xlUp).Row
  
  ' Restart Summaary_table_Row variable for 2nd loop
  
  Summary_Table_Row = 2

  ' Start another loop to get open price and close price

  For k = 2 To Lastrow
  
    ' Check if we are still within the Ticker, if it is not...
    If Cells(k + 1, 1).Value <> Cells(k, 1).Value Then

      Closeprice = Cells(k, 6).Value
      
      ' Print the yearly change in the summary table
      Range("J" & Summary_Table_Row).Value = Closeprice - Openprice
      
            If Openprice = 0 Then
            
            Range("K" & Summary_Table_Row).Value = FormatPercent(1)
            
            Else
            
            Range("K" & Summary_Table_Row).Value = FormatPercent((Closeprice - Openprice) / Openprice)
            
            End If

      ' Add one to the summary table row
      Summary_Table_Row = Summary_Table_Row + 1
      

    ' If the cell immediately following a row is the same brand...
    Else
            If Right(Cells(k, 2), 4) = "0101" Then

            Openprice = Cells(k, 3).Value
        
            End If

    End If

  Next k

  For m = 2 To Lastrow
  
    If Cells(m, 10) > 0 Then
  
        Cells(m, 10).Interior.ColorIndex = 4

    ElseIf Cells(m, 10) < 0 Then
    
        Cells(m, 10).Interior.ColorIndex = 3
    
    End If
    
  Next m

End Sub


