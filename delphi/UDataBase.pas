unit UDataBase;

interface

uses
  SysUtils, Classes, DB, ADODB;

type
  TDTM = class(TDataModule)
    Connection: TADOConnection;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  DTM: TDTM;

implementation

{$R *.dfm}

end.
