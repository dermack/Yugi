object frmLogin: TfrmLogin
  Left = 0
  Top = 0
  BorderStyle = bsToolWindow
  Caption = 'frmLogin'
  ClientHeight = 134
  ClientWidth = 333
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  Position = poDesktopCenter
  PixelsPerInch = 96
  TextHeight = 13
  object edtUser: TcxTextEdit
    Left = 20
    Top = 23
    TabOrder = 0
    OnKeyPress = edtUserKeyPress
    Width = 289
  end
  object cxLabel1: TcxLabel
    Left = 20
    Top = 5
    Caption = 'Usu'#225'rio'
    Transparent = True
  end
  object edtPass: TcxTextEdit
    Left = 20
    Top = 67
    Properties.EchoMode = eemPassword
    Properties.PasswordChar = '*'
    TabOrder = 2
    OnKeyPress = edtPassKeyPress
    Width = 289
  end
  object cxLabel2: TcxLabel
    Left = 20
    Top = 45
    Caption = 'Senha'
    Transparent = True
  end
  object btnEntrar: TcxButton
    Left = 88
    Top = 96
    Width = 75
    Height = 25
    Caption = 'Entrar'
    TabOrder = 4
    OnClick = btnEntrarClick
  end
  object btnSair: TcxButton
    Left = 169
    Top = 96
    Width = 75
    Height = 25
    Caption = 'Sair'
    TabOrder = 5
    OnClick = btnSairClick
  end
  object qryLogin: TADOQuery
    Connection = DTM.Connection
    Parameters = <>
    Left = 288
    Top = 104
  end
end
