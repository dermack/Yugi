program prjYugi;

uses
  Forms,
  UCadastroCarta in 'UCadastroCarta.pas' {frmCadastroCarta},
  UDataBase in 'UDataBase.pas' {DTM: TDataModule},
  UDeckEdit in 'UDeckEdit.pas' {frmDeckEdit},
  UMain in 'UMain.pas' {frmMain},
  ULogin in 'ULogin.pas' {frmLogin},
  UJogar in 'UJogar.pas' {Form1};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TDTM, DTM);
  Application.CreateForm(TfrmMain, frmMain);
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
