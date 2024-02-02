import { FC, useState } from 'react';
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from 'shadcn/components/ui/resizable';
import { PageHeader } from './PageHeader';
import { Sidebar } from './sidebar/Sidebar';
import { cn } from 'shadcn/lib/utils';

export const Layout: FC = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  return (
    <>
      <div className='h-full w-full flex flex-col'>
        <PageHeader />
        <div className='grow bg-apricot border border-gray-600'>
          <ResizablePanelGroup direction='horizontal' className='h-full'>
            <ResizablePanel
              defaultSize={15}
              minSize={10}
              maxSize={15}
              collapsible={true}
              collapsedSize={5}
              onCollapse={() => setIsCollapsed(true)}
              onExpand={() => setIsCollapsed(false)}
              className={cn('h-full flex flex-col', isCollapsed && 'min-w-10 transition-all duration-300 ease-in-out')}
            >
              <Sidebar isCollapsed={isCollapsed} />
            </ResizablePanel>
            <ResizableHandle />
            <ResizablePanel defaultSize={80}>Two</ResizablePanel>
          </ResizablePanelGroup>
        </div>
      </div>
    </>
  );
};
