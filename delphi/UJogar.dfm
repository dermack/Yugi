object Form1: TForm1
  Left = 0
  Top = 0
  Caption = 'Jogar'
  ClientHeight = 212
  ClientWidth = 418
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object qrySala: TADOQuery
    Connection = DTM.Connection
    Parameters = <>
    Left = 192
    Top = 16
  end
  object dsSala: TDataSource
    DataSet = qrySala
    Left = 80
    Top = 16
  end
end
